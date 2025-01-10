# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: tail_call
- machine: windows-amd64
- commit hash: ac80cdd
- commit date: 2025-01-10
- overall geometric mean: 1.039x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250110-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-ac80cdd |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 231 ms: 1.07x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.71 sec: 1.11x slower                                                     |
| html5lib       | 38.2 ms                                                     | 41.1 ms: 1.08x slower                                                      |
| sphinx         | 617 ms                                                      | 662 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250110-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-ac80cdd |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 216 ms: 1.30x faster                                                       |
| async_tree_io              | 513 ms                                                      | 421 ms: 1.22x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 412 ms: 1.21x faster                                                       |
| async_tree_none            | 219 ms                                                      | 189 ms: 1.16x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 233 ms: 1.14x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 177 ms: 1.13x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 350 ms: 1.09x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 354 ms: 1.07x faster                                                       |
| asyncio_websockets         | 300 ms                                                      | 310 ms: 1.03x slower                                                       |
| async_generators           | 223 ms                                                      | 236 ms: 1.06x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.10x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250110-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-ac80cdd |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 146 ms                                                      | 148 ms: 1.01x slower                                                       |
| float          | 50.8 ms                                                     | 53.0 ms: 1.04x slower                                                      |
| nbody          | 66.3 ms                                                     | 79.7 ms: 1.20x slower                                                      |
| Geometric mean | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250110-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-ac80cdd |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.69 ms                                                     | 1.48 ms: 1.15x faster                                                      |
| regex_dna      | 115 ms                                                      | 122 ms: 1.06x slower                                                       |
| regex_compile  | 80.7 ms                                                     | 89.7 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250110-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-ac80cdd |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 89.9 ms: 1.03x faster                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.8 ms: 1.05x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.47 sec: 1.07x slower                                                     |
| xml_etree_generate   | 53.5 ms                                                     | 58.1 ms: 1.09x slower                                                      |
| json_dumps           | 6.19 ms                                                     | 6.81 ms: 1.10x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 41.5 ms: 1.14x slower                                                      |
| unpickle_pure_python | 130 us                                                      | 153 us: 1.18x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 234 us: 1.26x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250110-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-ac80cdd |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 24.6 ms: 1.01x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 18.1 ms: 1.07x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250110-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-ac80cdd |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 35.3 ms: 1.04x slower                                                      |
| mako            | 6.56 ms                                                     | 7.09 ms: 1.08x slower                                                      |
| genshi_text     | 15.2 ms                                                     | 16.8 ms: 1.11x slower                                                      |
| django_template | 20.3 ms                                                     | 25.7 ms: 1.27x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.12x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250110-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-ac80cdd |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 530 us: 15.96x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 216 ms: 1.30x faster                                                       |
| async_tree_io              | 513 ms                                                      | 421 ms: 1.22x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 412 ms: 1.21x faster                                                       |
| deepcopy                   | 223 us                                                      | 188 us: 1.19x faster                                                       |
| async_tree_none            | 219 ms                                                      | 189 ms: 1.16x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.48 ms: 1.15x faster                                                      |
| async_tree_memoization     | 265 ms                                                      | 233 ms: 1.14x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 177 ms: 1.13x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 350 ms: 1.09x faster                                                       |
| json                       | 3.30 ms                                                     | 3.04 ms: 1.09x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 354 ms: 1.07x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 21.9 us: 1.05x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.92 us: 1.05x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 89.9 ms: 1.03x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.81 ms: 1.01x faster                                                      |
| pidigits                   | 146 ms                                                      | 148 ms: 1.01x slower                                                       |
| python_startup             | 24.4 ms                                                     | 24.6 ms: 1.01x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.24 ms: 1.01x slower                                                      |
| connected_components       | 320 ms                                                      | 324 ms: 1.01x slower                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.64 ms: 1.02x slower                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.61 us: 1.02x slower                                                      |
| mdp                        | 1.43 sec                                                    | 1.47 sec: 1.03x slower                                                     |
| spectral_norm              | 63.4 ms                                                     | 65.1 ms: 1.03x slower                                                      |
| asyncio_websockets         | 300 ms                                                      | 310 ms: 1.03x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 838 us: 1.03x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 35.3 ms: 1.04x slower                                                      |
| float                      | 50.8 ms                                                     | 53.0 ms: 1.04x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.8 ms: 1.05x slower                                                      |
| regex_dna                  | 115 ms                                                      | 122 ms: 1.06x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 3.04 sec: 1.06x slower                                                     |
| pathlib                    | 75.3 ms                                                     | 79.8 ms: 1.06x slower                                                      |
| async_generators           | 223 ms                                                      | 236 ms: 1.06x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 89.4 ms: 1.06x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 18.1 ms: 1.07x slower                                                      |
| 2to3                       | 215 ms                                                      | 231 ms: 1.07x slower                                                       |
| sphinx                     | 617 ms                                                      | 662 ms: 1.07x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.47 sec: 1.07x slower                                                     |
| typing_runtime_protocols   | 103 us                                                      | 111 us: 1.07x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 91.7 ms: 1.08x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                      |
| html5lib                   | 38.2 ms                                                     | 41.1 ms: 1.08x slower                                                      |
| mako                       | 6.56 ms                                                     | 7.09 ms: 1.08x slower                                                      |
| sympy_str                  | 167 ms                                                      | 181 ms: 1.08x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 43.4 ms: 1.08x slower                                                      |
| sympy_expand               | 286 ms                                                      | 310 ms: 1.08x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 58.1 ms: 1.09x slower                                                      |
| coverage                   | 45.3 ms                                                     | 49.3 ms: 1.09x slower                                                      |
| pycparser                  | 695 ms                                                      | 760 ms: 1.09x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 78.9 ms: 1.10x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 50.0 ms: 1.10x slower                                                      |
| json_dumps                 | 6.19 ms                                                     | 6.81 ms: 1.10x slower                                                      |
| fannkuch                   | 252 ms                                                      | 277 ms: 1.10x slower                                                       |
| scimark_fft                | 175 ms                                                      | 193 ms: 1.11x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 16.8 ms: 1.11x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 13.7 ms: 1.11x slower                                                      |
| regex_compile              | 80.7 ms                                                     | 89.7 ms: 1.11x slower                                                      |
| sqlglot_optimize           | 32.5 ms                                                     | 36.2 ms: 1.11x slower                                                      |
| go                         | 84.7 ms                                                     | 94.3 ms: 1.11x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.71 sec: 1.11x slower                                                     |
| xml_etree_process          | 36.5 ms                                                     | 41.5 ms: 1.14x slower                                                      |
| generators                 | 19.0 ms                                                     | 21.6 ms: 1.14x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 552 ms: 1.14x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 64.8 ms: 1.14x slower                                                      |
| logging_format             | 6.18 us                                                     | 7.07 us: 1.14x slower                                                      |
| sqlglot_normalize          | 172 ms                                                      | 197 ms: 1.15x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.65 us: 1.15x slower                                                      |
| pprint_pformat             | 977 ms                                                      | 1.13 sec: 1.15x slower                                                     |
| nqueens                    | 56.1 ms                                                     | 64.9 ms: 1.16x slower                                                      |
| pyflate                    | 283 ms                                                      | 331 ms: 1.17x slower                                                       |
| sqlglot_transpile          | 953 us                                                      | 1.12 ms: 1.18x slower                                                      |
| unpickle_pure_python       | 130 us                                                      | 153 us: 1.18x slower                                                       |
| sqlglot_parse              | 764 us                                                      | 912 us: 1.19x slower                                                       |
| nbody                      | 66.3 ms                                                     | 79.7 ms: 1.20x slower                                                      |
| chaos                      | 37.9 ms                                                     | 45.6 ms: 1.20x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 92.9 ms: 1.22x slower                                                      |
| comprehensions             | 10.4 us                                                     | 12.7 us: 1.22x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.69 ms: 1.22x slower                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 50.0 ms: 1.23x slower                                                      |
| richards_super             | 29.8 ms                                                     | 36.9 ms: 1.24x slower                                                      |
| many_optionals             | 361 us                                                      | 451 us: 1.25x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 234 us: 1.26x slower                                                       |
| richards                   | 26.3 ms                                                     | 33.1 ms: 1.26x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 69.1 ns: 1.27x slower                                                      |
| django_template            | 20.3 ms                                                     | 25.7 ms: 1.27x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.40 ms: 1.27x slower                                                      |
| raytrace                   | 153 ms                                                      | 211 ms: 1.37x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 16.8 ms: 1.55x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (6): json_loads, pylint, shortest_path, k_core, gc_traversal, regex_v8
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.039x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown