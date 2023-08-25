
# Results vs. 3.10.4

- fork: python
- ref: cdde29dde90947df9bac
- machine: darwin-arm64
- commit hash: cdde29d
- commit date: 2022-11-21
- overall geometric mean: 1.18x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 165 ms: 1.23x faster                                                   |
| chameleon      | 5.84 ms                                                | 4.42 ms: 1.32x faster                                                  |
| docutils       | 1.78 sec                                               | 1.47 sec: 1.21x faster                                                 |
| html5lib       | 44.1 ms                                                | 36.1 ms: 1.22x faster                                                  |
| tornado_http   | 91.9 ms                                                | 70.3 ms: 1.31x faster                                                  |
| Geometric mean | (ref)                                                  | 1.26x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 65.1 ms: 1.45x faster                                                  |
| float          | 72.3 ms                                                | 57.0 ms: 1.27x faster                                                  |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.23x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 75.7 ms: 1.28x faster                                                  |
| regex_v8       | 17.5 ms                                                | 15.8 ms: 1.11x faster                                                  |
| regex_dna      | 160 ms                                                 | 149 ms: 1.07x faster                                                   |
| regex_effbot   | 2.45 ms                                                | 2.65 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 8.38 ms                                                | 6.04 ms: 1.39x faster                                                  |
| pickle_pure_python   | 284 us                                                 | 208 us: 1.36x faster                                                   |
| xml_etree_process    | 45.1 ms                                                | 35.5 ms: 1.27x faster                                                  |
| unpickle_pure_python | 203 us                                                 | 161 us: 1.26x faster                                                   |
| xml_etree_parse      | 107 ms                                                 | 96.3 ms: 1.11x faster                                                  |
| xml_etree_generate   | 54.3 ms                                                | 49.3 ms: 1.10x faster                                                  |
| xml_etree_iterparse  | 72.6 ms                                                | 69.1 ms: 1.05x faster                                                  |
| json_loads           | 16.9 us                                                | 16.3 us: 1.03x faster                                                  |
| unpickle_list        | 2.66 us                                                | 2.63 us: 1.01x faster                                                  |
| pickle_list          | 2.83 us                                                | 2.81 us: 1.01x faster                                                  |
| unpickle             | 9.77 us                                                | 9.85 us: 1.01x slower                                                  |
| pickle_dict          | 17.8 us                                                | 17.9 us: 1.01x slower                                                  |
| pickle               | 7.36 us                                                | 7.51 us: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 12.2 ms: 1.03x faster                                                  |
| python_startup_no_site | 9.73 ms                                                | 10.2 ms: 1.04x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.21 ms: 1.45x faster                                                  |
| genshi_xml      | 37.6 ms                                                | 29.2 ms: 1.29x faster                                                  |
| django_template | 27.3 ms                                                | 21.4 ms: 1.28x faster                                                  |
| genshi_text     | 18.4 ms                                                | 14.6 ms: 1.26x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deltablue               | 5.15 ms                                                | 2.78 ms: 1.85x faster                                                  |
| logging_silent          | 119 ns                                                 | 64.6 ns: 1.85x faster                                                  |
| richards                | 51.4 ms                                                | 31.2 ms: 1.65x faster                                                  |
| raytrace                | 328 ms                                                 | 211 ms: 1.55x faster                                                   |
| scimark_lu              | 110 ms                                                 | 70.9 ms: 1.55x faster                                                  |
| async_tree_memoization  | 493 ms                                                 | 330 ms: 1.49x faster                                                   |
| crypto_pyaes            | 78.0 ms                                                | 53.1 ms: 1.47x faster                                                  |
| mako                    | 10.5 ms                                                | 7.21 ms: 1.45x faster                                                  |
| nbody                   | 94.1 ms                                                | 65.1 ms: 1.45x faster                                                  |
| go                      | 165 ms                                                 | 118 ms: 1.39x faster                                                   |
| async_tree_none         | 402 ms                                                 | 289 ms: 1.39x faster                                                   |
| json_dumps              | 8.38 ms                                                | 6.04 ms: 1.39x faster                                                  |
| async_tree_io           | 1.02 sec                                               | 745 ms: 1.37x faster                                                   |
| pickle_pure_python      | 284 us                                                 | 208 us: 1.36x faster                                                   |
| sqlglot_parse           | 1.33 ms                                                | 994 us: 1.34x faster                                                   |
| thrift                  | 586 us                                                 | 442 us: 1.33x faster                                                   |
| sqlglot_transpile       | 1.54 ms                                                | 1.16 ms: 1.33x faster                                                  |
| chameleon               | 5.84 ms                                                | 4.42 ms: 1.32x faster                                                  |
| scimark_monte_carlo     | 72.2 ms                                                | 54.7 ms: 1.32x faster                                                  |
| chaos                   | 66.8 ms                                                | 50.7 ms: 1.32x faster                                                  |
| pycparser               | 915 ms                                                 | 694 ms: 1.32x faster                                                   |
| spectral_norm           | 96.4 ms                                                | 73.2 ms: 1.32x faster                                                  |
| tornado_http            | 91.9 ms                                                | 70.3 ms: 1.31x faster                                                  |
| pyflate                 | 453 ms                                                 | 350 ms: 1.29x faster                                                   |
| genshi_xml              | 37.6 ms                                                | 29.2 ms: 1.29x faster                                                  |
| logging_simple          | 4.63 us                                                | 3.60 us: 1.28x faster                                                  |
| hexiom                  | 6.32 ms                                                | 4.93 ms: 1.28x faster                                                  |
| logging_format          | 5.01 us                                                | 3.91 us: 1.28x faster                                                  |
| django_template         | 27.3 ms                                                | 21.4 ms: 1.28x faster                                                  |
| regex_compile           | 96.6 ms                                                | 75.7 ms: 1.28x faster                                                  |
| float                   | 72.3 ms                                                | 57.0 ms: 1.27x faster                                                  |
| xml_etree_process       | 45.1 ms                                                | 35.5 ms: 1.27x faster                                                  |
| unpickle_pure_python    | 203 us                                                 | 161 us: 1.26x faster                                                   |
| genshi_text             | 18.4 ms                                                | 14.6 ms: 1.26x faster                                                  |
| create_gc_cycles        | 876 us                                                 | 695 us: 1.26x faster                                                   |
| scimark_sparse_mat_mult | 3.47 ms                                                | 2.82 ms: 1.23x faster                                                  |
| async_tree_cpu_io_mixed | 670 ms                                                 | 544 ms: 1.23x faster                                                   |
| dulwich_log             | 37.1 ms                                                | 30.2 ms: 1.23x faster                                                  |
| 2to3                    | 202 ms                                                 | 165 ms: 1.23x faster                                                   |
| pprint_safe_repr        | 609 ms                                                 | 497 ms: 1.22x faster                                                   |
| pprint_pformat          | 1.24 sec                                               | 1.01 sec: 1.22x faster                                                 |
| scimark_sor             | 127 ms                                                 | 104 ms: 1.22x faster                                                   |
| html5lib                | 44.1 ms                                                | 36.1 ms: 1.22x faster                                                  |
| docutils                | 1.78 sec                                               | 1.47 sec: 1.21x faster                                                 |
| sqlglot_optimize        | 38.0 ms                                                | 31.4 ms: 1.21x faster                                                  |
| deepcopy_memo           | 34.5 us                                                | 29.0 us: 1.19x faster                                                  |
| mypy2                   | 308 ms                                                 | 263 ms: 1.17x faster                                                   |
| fannkuch                | 317 ms                                                 | 271 ms: 1.17x faster                                                   |
| scimark_fft             | 232 ms                                                 | 198 ms: 1.17x faster                                                   |
| bench_thread_pool       | 548 us                                                 | 470 us: 1.17x faster                                                   |
| deepcopy_reduce         | 2.38 us                                                | 2.07 us: 1.15x faster                                                  |
| sympy_integrate         | 13.4 ms                                                | 11.7 ms: 1.14x faster                                                  |
| deepcopy                | 278 us                                                 | 244 us: 1.14x faster                                                   |
| sqlglot_normalize       | 197 ms                                                 | 173 ms: 1.14x faster                                                   |
| async_generators        | 233 ms                                                 | 205 ms: 1.14x faster                                                   |
| dask                    | 258 ms                                                 | 228 ms: 1.13x faster                                                   |
| xml_etree_parse         | 107 ms                                                 | 96.3 ms: 1.11x faster                                                  |
| sympy_expand            | 276 ms                                                 | 247 ms: 1.11x faster                                                   |
| regex_v8                | 17.5 ms                                                | 15.8 ms: 1.11x faster                                                  |
| nqueens                 | 68.1 ms                                                | 61.8 ms: 1.10x faster                                                  |
| xml_etree_generate      | 54.3 ms                                                | 49.3 ms: 1.10x faster                                                  |
| json                    | 3.10 ms                                                | 2.82 ms: 1.10x faster                                                  |
| sympy_str               | 169 ms                                                 | 154 ms: 1.10x faster                                                   |
| telco                   | 3.68 ms                                                | 3.37 ms: 1.09x faster                                                  |
| mdp                     | 1.67 sec                                               | 1.54 sec: 1.08x faster                                                 |
| sympy_sum               | 94.3 ms                                                | 87.0 ms: 1.08x faster                                                  |
| regex_dna               | 160 ms                                                 | 149 ms: 1.07x faster                                                   |
| pathlib                 | 28.8 ms                                                | 27.1 ms: 1.06x faster                                                  |
| sqlite_synth            | 1.47 us                                                | 1.39 us: 1.06x faster                                                  |
| xml_etree_iterparse     | 72.6 ms                                                | 69.1 ms: 1.05x faster                                                  |
| json_loads              | 16.9 us                                                | 16.3 us: 1.03x faster                                                  |
| python_startup          | 12.6 ms                                                | 12.2 ms: 1.03x faster                                                  |
| asyncio_tcp             | 673 ms                                                 | 652 ms: 1.03x faster                                                   |
| meteor_contest          | 78.6 ms                                                | 77.2 ms: 1.02x faster                                                  |
| coroutines              | 20.2 ms                                                | 19.9 ms: 1.01x faster                                                  |
| unpickle_list           | 2.66 us                                                | 2.63 us: 1.01x faster                                                  |
| pickle_list             | 2.83 us                                                | 2.81 us: 1.01x faster                                                  |
| pidigits                | 282 ms                                                 | 281 ms: 1.00x faster                                                   |
| comprehensions          | 17.7 us                                                | 17.8 us: 1.01x slower                                                  |
| gc_traversal            | 2.40 ms                                                | 2.42 ms: 1.01x slower                                                  |
| unpickle                | 9.77 us                                                | 9.85 us: 1.01x slower                                                  |
| pickle_dict             | 17.8 us                                                | 17.9 us: 1.01x slower                                                  |
| pickle                  | 7.36 us                                                | 7.51 us: 1.02x slower                                                  |
| generators              | 32.9 ms                                                | 34.3 ms: 1.04x slower                                                  |
| python_startup_no_site  | 9.73 ms                                                | 10.2 ms: 1.04x slower                                                  |
| bench_mp_pool           | 41.0 ms                                                | 44.3 ms: 1.08x slower                                                  |
| regex_effbot            | 2.45 ms                                                | 2.65 ms: 1.08x slower                                                  |
| coverage                | 40.8 ms                                                | 57.4 ms: 1.41x slower                                                  |
| unpack_sequence         | 38.7 ns                                                | 62.4 ns: 1.61x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.18x faster                                                           |
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.14x
