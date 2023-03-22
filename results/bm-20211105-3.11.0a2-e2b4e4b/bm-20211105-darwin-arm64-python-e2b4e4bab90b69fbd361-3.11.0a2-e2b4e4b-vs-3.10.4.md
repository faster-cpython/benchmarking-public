
# Results vs. 3.10.4

- fork: python
- ref: e2b4e4bab90b69fbd361
- machine: darwin-arm64
- commit hash: e2b4e4b
- commit date: 2021-11-05
- overall geometric mean: 1.15x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 166 ms: 1.21x faster                                                  |
| chameleon      | 5.79 ms                                                | 5.09 ms: 1.14x faster                                                 |
| docutils       | 1.78 sec                                               | 1.54 sec: 1.16x faster                                                |
| html5lib       | 44.2 ms                                                | 36.7 ms: 1.21x faster                                                 |
| tornado_http   | 91.5 ms                                                | 76.5 ms: 1.20x faster                                                 |
| Geometric mean | (ref)                                                  | 1.18x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 52.0 ms: 1.39x faster                                                 |
| nbody          | 93.3 ms                                                | 74.3 ms: 1.26x faster                                                 |
| pidigits       | 282 ms                                                 | 281 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.21x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 78.0 ms: 1.24x faster                                                 |
| regex_v8       | 17.6 ms                                                | 17.5 ms: 1.00x faster                                                 |
| regex_effbot   | 2.46 ms                                                | 2.45 ms: 1.00x faster                                                 |
| regex_dna      | 162 ms                                                 | 162 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 229 us: 1.24x faster                                                  |
| xml_etree_process    | 44.8 ms                                                | 36.9 ms: 1.21x faster                                                 |
| unpickle_pure_python | 203 us                                                 | 176 us: 1.16x faster                                                  |
| xml_etree_generate   | 54.2 ms                                                | 48.8 ms: 1.11x faster                                                 |
| json_dumps           | 8.40 ms                                                | 7.85 ms: 1.07x faster                                                 |
| unpickle_list        | 2.69 us                                                | 2.52 us: 1.07x faster                                                 |
| xml_etree_parse      | 106 ms                                                 | 101 ms: 1.05x faster                                                  |
| xml_etree_iterparse  | 72.3 ms                                                | 69.8 ms: 1.03x faster                                                 |
| json_loads           | 16.9 us                                                | 16.6 us: 1.02x faster                                                 |
| pickle_dict          | 17.9 us                                                | 17.6 us: 1.02x faster                                                 |
| pickle               | 7.35 us                                                | 7.26 us: 1.01x faster                                                 |
| unpickle             | 9.89 us                                                | 10.1 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 8.88 ms                                                | 9.29 ms: 1.05x slower                                                 |
| python_startup         | 11.9 ms                                                | 15.9 ms: 1.33x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.18x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 10.5 ms                                                | 8.55 ms: 1.23x faster                                                 |
| django_template | 27.3 ms                                                | 22.7 ms: 1.20x faster                                                 |
| genshi_xml      | 37.2 ms                                                | 30.9 ms: 1.20x faster                                                 |
| genshi_text     | 18.4 ms                                                | 15.7 ms: 1.17x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.20x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 3.23 ms: 1.59x faster                                                 |
| raytrace                | 325 ms                                                 | 209 ms: 1.56x faster                                                  |
| scimark_monte_carlo     | 72.5 ms                                                | 49.2 ms: 1.47x faster                                                 |
| logging_silent          | 119 ns                                                 | 82.2 ns: 1.45x faster                                                 |
| float                   | 72.4 ms                                                | 52.0 ms: 1.39x faster                                                 |
| go                      | 165 ms                                                 | 119 ms: 1.39x faster                                                  |
| richards                | 51.4 ms                                                | 37.7 ms: 1.36x faster                                                 |
| async_tree_none         | 400 ms                                                 | 294 ms: 1.36x faster                                                  |
| chaos                   | 66.7 ms                                                | 49.2 ms: 1.36x faster                                                 |
| crypto_pyaes            | 78.1 ms                                                | 58.2 ms: 1.34x faster                                                 |
| async_tree_memoization  | 490 ms                                                 | 367 ms: 1.34x faster                                                  |
| logging_simple          | 4.63 us                                                | 3.47 us: 1.33x faster                                                 |
| logging_format          | 4.97 us                                                | 3.73 us: 1.33x faster                                                 |
| async_tree_io           | 1.02 sec                                               | 794 ms: 1.28x faster                                                  |
| hexiom                  | 6.32 ms                                                | 4.93 ms: 1.28x faster                                                 |
| spectral_norm           | 95.8 ms                                                | 75.1 ms: 1.28x faster                                                 |
| scimark_sor             | 126 ms                                                 | 99.5 ms: 1.27x faster                                                 |
| pyflate                 | 453 ms                                                 | 360 ms: 1.26x faster                                                  |
| nbody                   | 93.3 ms                                                | 74.3 ms: 1.26x faster                                                 |
| thrift                  | 580 us                                                 | 467 us: 1.24x faster                                                  |
| pickle_pure_python      | 283 us                                                 | 229 us: 1.24x faster                                                  |
| deepcopy_memo           | 34.4 us                                                | 27.8 us: 1.24x faster                                                 |
| regex_compile           | 96.4 ms                                                | 78.0 ms: 1.24x faster                                                 |
| mako                    | 10.5 ms                                                | 8.55 ms: 1.23x faster                                                 |
| pprint_safe_repr        | 606 ms                                                 | 499 ms: 1.21x faster                                                  |
| xml_etree_process       | 44.8 ms                                                | 36.9 ms: 1.21x faster                                                 |
| 2to3                    | 201 ms                                                 | 166 ms: 1.21x faster                                                  |
| pprint_pformat          | 1.23 sec                                               | 1.02 sec: 1.21x faster                                                |
| html5lib                | 44.2 ms                                                | 36.7 ms: 1.21x faster                                                 |
| django_template         | 27.3 ms                                                | 22.7 ms: 1.20x faster                                                 |
| genshi_xml              | 37.2 ms                                                | 30.9 ms: 1.20x faster                                                 |
| unpack_sequence         | 37.4 ns                                                | 31.3 ns: 1.20x faster                                                 |
| create_gc_cycles        | 880 us                                                 | 735 us: 1.20x faster                                                  |
| tornado_http            | 91.5 ms                                                | 76.5 ms: 1.20x faster                                                 |
| pycparser               | 916 ms                                                 | 767 ms: 1.19x faster                                                  |
| dulwich_log             | 37.1 ms                                                | 31.3 ms: 1.18x faster                                                 |
| async_generators        | 234 ms                                                 | 198 ms: 1.18x faster                                                  |
| deepcopy                | 281 us                                                 | 239 us: 1.18x faster                                                  |
| gunicorn                | 1.35 ms                                                | 1.15 ms: 1.18x faster                                                 |
| genshi_text             | 18.4 ms                                                | 15.7 ms: 1.17x faster                                                 |
| scimark_lu              | 109 ms                                                 | 93.8 ms: 1.17x faster                                                 |
| deepcopy_reduce         | 2.37 us                                                | 2.05 us: 1.16x faster                                                 |
| unpickle_pure_python    | 203 us                                                 | 176 us: 1.16x faster                                                  |
| sqlalchemy_imperative   | 8.89 ms                                                | 7.69 ms: 1.16x faster                                                 |
| docutils                | 1.78 sec                                               | 1.54 sec: 1.16x faster                                                |
| generators              | 32.7 ms                                                | 28.5 ms: 1.15x faster                                                 |
| sqlalchemy_declarative  | 74.9 ms                                                | 65.3 ms: 1.15x faster                                                 |
| scimark_fft             | 230 ms                                                 | 201 ms: 1.15x faster                                                  |
| async_tree_cpu_io_mixed | 669 ms                                                 | 587 ms: 1.14x faster                                                  |
| chameleon               | 5.79 ms                                                | 5.09 ms: 1.14x faster                                                 |
| fannkuch                | 317 ms                                                 | 279 ms: 1.14x faster                                                  |
| sqlglot_optimize        | 38.0 ms                                                | 33.6 ms: 1.13x faster                                                 |
| sqlglot_normalize       | 196 ms                                                 | 175 ms: 1.12x faster                                                  |
| sqlglot_transpile       | 1.57 ms                                                | 1.41 ms: 1.11x faster                                                 |
| xml_etree_generate      | 54.2 ms                                                | 48.8 ms: 1.11x faster                                                 |
| nqueens                 | 68.2 ms                                                | 61.6 ms: 1.11x faster                                                 |
| flaskblogging           | 2.75 ms                                                | 2.49 ms: 1.11x faster                                                 |
| sqlglot_parse           | 1.37 ms                                                | 1.24 ms: 1.10x faster                                                 |
| sympy_integrate         | 13.3 ms                                                | 12.1 ms: 1.09x faster                                                 |
| pathlib                 | 28.8 ms                                                | 26.5 ms: 1.09x faster                                                 |
| pylint                  | 307 ms                                                 | 283 ms: 1.09x faster                                                  |
| sympy_sum               | 93.6 ms                                                | 86.3 ms: 1.08x faster                                                 |
| sympy_expand            | 275 ms                                                 | 256 ms: 1.08x faster                                                  |
| telco                   | 3.63 ms                                                | 3.39 ms: 1.07x faster                                                 |
| sqlite_synth            | 1.47 us                                                | 1.38 us: 1.07x faster                                                 |
| json_dumps              | 8.40 ms                                                | 7.85 ms: 1.07x faster                                                 |
| sympy_str               | 169 ms                                                 | 158 ms: 1.07x faster                                                  |
| unpickle_list           | 2.69 us                                                | 2.52 us: 1.07x faster                                                 |
| scimark_sparse_mat_mult | 3.46 ms                                                | 3.25 ms: 1.06x faster                                                 |
| bench_thread_pool       | 546 us                                                 | 516 us: 1.06x faster                                                  |
| mdp                     | 1.66 sec                                               | 1.57 sec: 1.06x faster                                                |
| meteor_contest          | 78.1 ms                                                | 74.2 ms: 1.05x faster                                                 |
| xml_etree_parse         | 106 ms                                                 | 101 ms: 1.05x faster                                                  |
| coroutines              | 20.2 ms                                                | 19.3 ms: 1.05x faster                                                 |
| xml_etree_iterparse     | 72.3 ms                                                | 69.8 ms: 1.03x faster                                                 |
| json                    | 3.08 ms                                                | 2.98 ms: 1.03x faster                                                 |
| json_loads              | 16.9 us                                                | 16.6 us: 1.02x faster                                                 |
| pickle_dict             | 17.9 us                                                | 17.6 us: 1.02x faster                                                 |
| pickle                  | 7.35 us                                                | 7.26 us: 1.01x faster                                                 |
| pidigits                | 282 ms                                                 | 281 ms: 1.01x faster                                                  |
| regex_v8                | 17.6 ms                                                | 17.5 ms: 1.00x faster                                                 |
| regex_effbot            | 2.46 ms                                                | 2.45 ms: 1.00x faster                                                 |
| regex_dna               | 162 ms                                                 | 162 ms: 1.00x slower                                                  |
| gc_traversal            | 2.39 ms                                                | 2.43 ms: 1.01x slower                                                 |
| unpickle                | 9.89 us                                                | 10.1 us: 1.02x slower                                                 |
| coverage                | 42.0 ms                                                | 43.4 ms: 1.03x slower                                                 |
| python_startup_no_site  | 8.88 ms                                                | 9.29 ms: 1.05x slower                                                 |
| bench_mp_pool           | 39.7 ms                                                | 42.0 ms: 1.06x slower                                                 |
| dask                    | 265 ms                                                 | 290 ms: 1.09x slower                                                  |
| python_startup          | 11.9 ms                                                | 15.9 ms: 1.33x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.15x faster                                                          |

Benchmark hidden because not significant (2): comprehensions, pickle_list
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, mypy2
