
# Results vs. 3.10.4

- fork: python
- ref: cdde29dde90947df9bac
- machine: darwin-arm64
- commit hash: cdde29d
- commit date: 2022-11-21
- overall geometric mean: 1.18x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 165 ms: 1.22x faster                                                   |
| chameleon      | 5.79 ms                                                | 4.42 ms: 1.31x faster                                                  |
| docutils       | 1.78 sec                                               | 1.47 sec: 1.21x faster                                                 |
| html5lib       | 44.2 ms                                                | 36.1 ms: 1.23x faster                                                  |
| tornado_http   | 91.5 ms                                                | 70.3 ms: 1.30x faster                                                  |
| Geometric mean | (ref)                                                  | 1.25x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 65.1 ms: 1.43x faster                                                  |
| float          | 72.4 ms                                                | 57.0 ms: 1.27x faster                                                  |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.22x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 75.7 ms: 1.27x faster                                                  |
| regex_v8       | 17.6 ms                                                | 15.8 ms: 1.11x faster                                                  |
| regex_dna      | 162 ms                                                 | 149 ms: 1.08x faster                                                   |
| regex_effbot   | 2.46 ms                                                | 2.65 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 8.40 ms                                                | 6.04 ms: 1.39x faster                                                  |
| pickle_pure_python   | 283 us                                                 | 208 us: 1.36x faster                                                   |
| unpickle_pure_python | 203 us                                                 | 161 us: 1.26x faster                                                   |
| xml_etree_process    | 44.8 ms                                                | 35.5 ms: 1.26x faster                                                  |
| xml_etree_parse      | 106 ms                                                 | 96.3 ms: 1.11x faster                                                  |
| xml_etree_generate   | 54.2 ms                                                | 49.3 ms: 1.10x faster                                                  |
| xml_etree_iterparse  | 72.3 ms                                                | 69.1 ms: 1.05x faster                                                  |
| json_loads           | 16.9 us                                                | 16.3 us: 1.03x faster                                                  |
| unpickle_list        | 2.69 us                                                | 2.63 us: 1.02x faster                                                  |
| pickle_dict          | 17.9 us                                                | 17.9 us: 1.00x slower                                                  |
| pickle               | 7.35 us                                                | 7.51 us: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                           |

Benchmark hidden because not significant (2): unpickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 12.2 ms: 1.03x slower                                                  |
| python_startup_no_site | 8.88 ms                                                | 10.2 ms: 1.14x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.21 ms: 1.45x faster                                                  |
| django_template | 27.3 ms                                                | 21.4 ms: 1.28x faster                                                  |
| genshi_xml      | 37.2 ms                                                | 29.2 ms: 1.27x faster                                                  |
| genshi_text     | 18.4 ms                                                | 14.6 ms: 1.26x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.31x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| logging_silent          | 119 ns                                                 | 64.6 ns: 1.85x faster                                                  |
| deltablue               | 5.14 ms                                                | 2.78 ms: 1.85x faster                                                  |
| richards                | 51.4 ms                                                | 31.2 ms: 1.65x faster                                                  |
| scimark_lu              | 109 ms                                                 | 70.9 ms: 1.54x faster                                                  |
| raytrace                | 325 ms                                                 | 211 ms: 1.54x faster                                                   |
| async_tree_memoization  | 490 ms                                                 | 330 ms: 1.48x faster                                                   |
| crypto_pyaes            | 78.1 ms                                                | 53.1 ms: 1.47x faster                                                  |
| mako                    | 10.5 ms                                                | 7.21 ms: 1.45x faster                                                  |
| nbody                   | 93.3 ms                                                | 65.1 ms: 1.43x faster                                                  |
| go                      | 165 ms                                                 | 118 ms: 1.40x faster                                                   |
| json_dumps              | 8.40 ms                                                | 6.04 ms: 1.39x faster                                                  |
| async_tree_none         | 400 ms                                                 | 289 ms: 1.39x faster                                                   |
| sqlglot_parse           | 1.37 ms                                                | 994 us: 1.37x faster                                                   |
| async_tree_io           | 1.02 sec                                               | 745 ms: 1.37x faster                                                   |
| pickle_pure_python      | 283 us                                                 | 208 us: 1.36x faster                                                   |
| sqlglot_transpile       | 1.57 ms                                                | 1.16 ms: 1.36x faster                                                  |
| scimark_monte_carlo     | 72.5 ms                                                | 54.7 ms: 1.33x faster                                                  |
| pycparser               | 916 ms                                                 | 694 ms: 1.32x faster                                                   |
| chaos                   | 66.7 ms                                                | 50.7 ms: 1.32x faster                                                  |
| thrift                  | 580 us                                                 | 442 us: 1.31x faster                                                   |
| chameleon               | 5.79 ms                                                | 4.42 ms: 1.31x faster                                                  |
| spectral_norm           | 95.8 ms                                                | 73.2 ms: 1.31x faster                                                  |
| tornado_http            | 91.5 ms                                                | 70.3 ms: 1.30x faster                                                  |
| pyflate                 | 453 ms                                                 | 350 ms: 1.29x faster                                                   |
| logging_simple          | 4.63 us                                                | 3.60 us: 1.28x faster                                                  |
| hexiom                  | 6.32 ms                                                | 4.93 ms: 1.28x faster                                                  |
| django_template         | 27.3 ms                                                | 21.4 ms: 1.28x faster                                                  |
| regex_compile           | 96.4 ms                                                | 75.7 ms: 1.27x faster                                                  |
| genshi_xml              | 37.2 ms                                                | 29.2 ms: 1.27x faster                                                  |
| float                   | 72.4 ms                                                | 57.0 ms: 1.27x faster                                                  |
| logging_format          | 4.97 us                                                | 3.91 us: 1.27x faster                                                  |
| create_gc_cycles        | 880 us                                                 | 695 us: 1.27x faster                                                   |
| unpickle_pure_python    | 203 us                                                 | 161 us: 1.26x faster                                                   |
| xml_etree_process       | 44.8 ms                                                | 35.5 ms: 1.26x faster                                                  |
| genshi_text             | 18.4 ms                                                | 14.6 ms: 1.26x faster                                                  |
| async_tree_cpu_io_mixed | 669 ms                                                 | 544 ms: 1.23x faster                                                   |
| scimark_sparse_mat_mult | 3.46 ms                                                | 2.82 ms: 1.23x faster                                                  |
| dulwich_log             | 37.1 ms                                                | 30.2 ms: 1.23x faster                                                  |
| html5lib                | 44.2 ms                                                | 36.1 ms: 1.23x faster                                                  |
| 2to3                    | 201 ms                                                 | 165 ms: 1.22x faster                                                   |
| pprint_safe_repr        | 606 ms                                                 | 497 ms: 1.22x faster                                                   |
| scimark_sor             | 126 ms                                                 | 104 ms: 1.22x faster                                                   |
| pprint_pformat          | 1.23 sec                                               | 1.01 sec: 1.22x faster                                                 |
| sqlglot_optimize        | 38.0 ms                                                | 31.4 ms: 1.21x faster                                                  |
| docutils                | 1.78 sec                                               | 1.47 sec: 1.21x faster                                                 |
| deepcopy_memo           | 34.4 us                                                | 29.0 us: 1.19x faster                                                  |
| fannkuch                | 317 ms                                                 | 271 ms: 1.17x faster                                                   |
| mypy2                   | 307 ms                                                 | 263 ms: 1.16x faster                                                   |
| bench_thread_pool       | 546 us                                                 | 470 us: 1.16x faster                                                   |
| dask                    | 265 ms                                                 | 228 ms: 1.16x faster                                                   |
| scimark_fft             | 230 ms                                                 | 198 ms: 1.16x faster                                                   |
| deepcopy                | 281 us                                                 | 244 us: 1.15x faster                                                   |
| deepcopy_reduce         | 2.37 us                                                | 2.07 us: 1.15x faster                                                  |
| async_generators        | 234 ms                                                 | 205 ms: 1.14x faster                                                   |
| sqlglot_normalize       | 196 ms                                                 | 173 ms: 1.14x faster                                                   |
| sympy_integrate         | 13.3 ms                                                | 11.7 ms: 1.13x faster                                                  |
| sympy_expand            | 275 ms                                                 | 247 ms: 1.11x faster                                                   |
| regex_v8                | 17.6 ms                                                | 15.8 ms: 1.11x faster                                                  |
| xml_etree_parse         | 106 ms                                                 | 96.3 ms: 1.11x faster                                                  |
| nqueens                 | 68.2 ms                                                | 61.8 ms: 1.10x faster                                                  |
| xml_etree_generate      | 54.2 ms                                                | 49.3 ms: 1.10x faster                                                  |
| sympy_str               | 169 ms                                                 | 154 ms: 1.10x faster                                                   |
| json                    | 3.08 ms                                                | 2.82 ms: 1.09x faster                                                  |
| regex_dna               | 162 ms                                                 | 149 ms: 1.08x faster                                                   |
| mdp                     | 1.66 sec                                               | 1.54 sec: 1.08x faster                                                 |
| telco                   | 3.63 ms                                                | 3.37 ms: 1.08x faster                                                  |
| sympy_sum               | 93.6 ms                                                | 87.0 ms: 1.08x faster                                                  |
| pathlib                 | 28.8 ms                                                | 27.1 ms: 1.06x faster                                                  |
| sqlite_synth            | 1.47 us                                                | 1.39 us: 1.06x faster                                                  |
| xml_etree_iterparse     | 72.3 ms                                                | 69.1 ms: 1.05x faster                                                  |
| json_loads              | 16.9 us                                                | 16.3 us: 1.03x faster                                                  |
| asyncio_tcp             | 670 ms                                                 | 652 ms: 1.03x faster                                                   |
| unpickle_list           | 2.69 us                                                | 2.63 us: 1.02x faster                                                  |
| coroutines              | 20.2 ms                                                | 19.9 ms: 1.01x faster                                                  |
| meteor_contest          | 78.1 ms                                                | 77.2 ms: 1.01x faster                                                  |
| pidigits                | 282 ms                                                 | 281 ms: 1.00x faster                                                   |
| pickle_dict             | 17.9 us                                                | 17.9 us: 1.00x slower                                                  |
| gc_traversal            | 2.39 ms                                                | 2.42 ms: 1.01x slower                                                  |
| comprehensions          | 17.6 us                                                | 17.8 us: 1.01x slower                                                  |
| pickle                  | 7.35 us                                                | 7.51 us: 1.02x slower                                                  |
| python_startup          | 11.9 ms                                                | 12.2 ms: 1.03x slower                                                  |
| generators              | 32.7 ms                                                | 34.3 ms: 1.05x slower                                                  |
| regex_effbot            | 2.46 ms                                                | 2.65 ms: 1.08x slower                                                  |
| bench_mp_pool           | 39.7 ms                                                | 44.3 ms: 1.11x slower                                                  |
| python_startup_no_site  | 8.88 ms                                                | 10.2 ms: 1.14x slower                                                  |
| coverage                | 42.0 ms                                                | 57.4 ms: 1.36x slower                                                  |
| unpack_sequence         | 37.4 ns                                                | 62.4 ns: 1.67x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.18x faster                                                           |

Benchmark hidden because not significant (2): unpickle, pickle_list
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
