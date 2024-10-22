# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: fix_unsafe_refcounti
- machine: windows-amd64
- commit hash: 8278d07
- commit date: 2024-10-12
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 229 ms: 1.06x slower                                                                 |
| docutils       | 1.57 sec                                                    | 1.72 sec: 1.09x slower                                                               |
| html5lib       | 38.6 ms                                                     | 43.8 ms: 1.13x slower                                                                |
| tornado_http   | 92.8 ms                                                     | 94.1 ms: 1.01x slower                                                                |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 259 ms: 1.11x faster                                                                 |
| async_tree_none            | 223 ms                                                      | 214 ms: 1.05x faster                                                                 |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 396 ms: 1.02x slower                                                                 |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 395 ms: 1.05x slower                                                                 |
| async_tree_io_tg           | 512 ms                                                      | 581 ms: 1.13x slower                                                                 |
| async_generators           | 223 ms                                                      | 253 ms: 1.13x slower                                                                 |
| async_tree_io              | 521 ms                                                      | 594 ms: 1.14x slower                                                                 |
| coroutines                 | 12.5 ms                                                     | 14.3 ms: 1.14x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                                         |

Benchmark hidden because not significant (4): asyncio_tcp, async_tree_memoization, async_tree_none_tg, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 48.1 ms                                                     | 54.1 ms: 1.13x slower                                                                |
| nbody          | 64.5 ms                                                     | 82.9 ms: 1.29x slower                                                                |
| Geometric mean | (ref)                                                       | 1.13x slower                                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                                |
| regex_v8       | 14.7 ms                                                     | 14.9 ms: 1.02x slower                                                                |
| regex_compile  | 80.1 ms                                                     | 90.8 ms: 1.13x slower                                                                |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                         |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pickle               | 7.34 us                                                     | 7.45 us: 1.01x slower                                                                |
| unpickle_list        | 2.72 us                                                     | 2.77 us: 1.02x slower                                                                |
| xml_etree_parse      | 93.2 ms                                                     | 96.2 ms: 1.03x slower                                                                |
| json_loads           | 14.3 us                                                     | 14.8 us: 1.04x slower                                                                |
| pickle_dict          | 18.0 us                                                     | 19.3 us: 1.07x slower                                                                |
| xml_etree_iterparse  | 62.3 ms                                                     | 67.0 ms: 1.07x slower                                                                |
| xml_etree_generate   | 53.3 ms                                                     | 58.0 ms: 1.09x slower                                                                |
| unpickle             | 8.63 us                                                     | 9.47 us: 1.10x slower                                                                |
| xml_etree_process    | 36.5 ms                                                     | 41.0 ms: 1.12x slower                                                                |
| json_dumps           | 5.76 ms                                                     | 6.73 ms: 1.17x slower                                                                |
| unpickle_pure_python | 127 us                                                      | 149 us: 1.17x slower                                                                 |
| pickle_pure_python   | 183 us                                                      | 217 us: 1.19x slower                                                                 |
| tomli_loads          | 1.36 sec                                                    | 1.65 sec: 1.21x slower                                                               |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                                         |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 17.8 ms                                                     | 18.0 ms: 1.02x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.01x slower                                                                         |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 6.79 ms: 1.09x slower                                                                |
| genshi_xml      | 32.8 ms                                                     | 37.1 ms: 1.13x slower                                                                |
| genshi_text     | 14.9 ms                                                     | 17.4 ms: 1.17x slower                                                                |
| django_template | 21.8 ms                                                     | 26.3 ms: 1.21x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.15x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 524 us: 16.57x faster                                                                |
| deepcopy                   | 223 us                                                      | 193 us: 1.16x faster                                                                 |
| async_tree_memoization_tg  | 288 ms                                                      | 259 ms: 1.11x faster                                                                 |
| deepcopy_memo              | 21.8 us                                                     | 19.9 us: 1.10x faster                                                                |
| unpack_sequence            | 40.0 ns                                                     | 37.5 ns: 1.07x faster                                                                |
| async_tree_none            | 223 ms                                                      | 214 ms: 1.05x faster                                                                 |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                                |
| bench_mp_pool              | 69.6 ms                                                     | 68.7 ms: 1.01x faster                                                                |
| telco                      | 4.85 ms                                                     | 4.79 ms: 1.01x faster                                                                |
| pathlib                    | 81.2 ms                                                     | 80.6 ms: 1.01x faster                                                                |
| tornado_http               | 92.8 ms                                                     | 94.1 ms: 1.01x slower                                                                |
| pickle                     | 7.34 us                                                     | 7.45 us: 1.01x slower                                                                |
| python_startup_no_site     | 17.8 ms                                                     | 18.0 ms: 1.02x slower                                                                |
| regex_v8                   | 14.7 ms                                                     | 14.9 ms: 1.02x slower                                                                |
| unpickle_list              | 2.72 us                                                     | 2.77 us: 1.02x slower                                                                |
| go                         | 84.6 ms                                                     | 86.4 ms: 1.02x slower                                                                |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 396 ms: 1.02x slower                                                                 |
| xml_etree_parse            | 93.2 ms                                                     | 96.2 ms: 1.03x slower                                                                |
| json_loads                 | 14.3 us                                                     | 14.8 us: 1.04x slower                                                                |
| sympy_sum                  | 86.4 ms                                                     | 89.8 ms: 1.04x slower                                                                |
| coverage                   | 46.7 ms                                                     | 48.6 ms: 1.04x slower                                                                |
| sqlite_synth               | 1.60 us                                                     | 1.68 us: 1.05x slower                                                                |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 395 ms: 1.05x slower                                                                 |
| 2to3                       | 217 ms                                                      | 229 ms: 1.06x slower                                                                 |
| pickle_dict                | 18.0 us                                                     | 19.3 us: 1.07x slower                                                                |
| sympy_str                  | 166 ms                                                      | 178 ms: 1.07x slower                                                                 |
| meteor_contest             | 72.3 ms                                                     | 77.6 ms: 1.07x slower                                                                |
| xml_etree_iterparse        | 62.3 ms                                                     | 67.0 ms: 1.07x slower                                                                |
| sympy_expand               | 285 ms                                                      | 307 ms: 1.08x slower                                                                 |
| pylint                     | 211 ms                                                      | 228 ms: 1.08x slower                                                                 |
| dulwich_log                | 40.4 ms                                                     | 43.9 ms: 1.09x slower                                                                |
| xml_etree_generate         | 53.3 ms                                                     | 58.0 ms: 1.09x slower                                                                |
| mako                       | 6.24 ms                                                     | 6.79 ms: 1.09x slower                                                                |
| docutils                   | 1.57 sec                                                    | 1.72 sec: 1.09x slower                                                               |
| unpickle                   | 8.63 us                                                     | 9.47 us: 1.10x slower                                                                |
| mdp                        | 1.38 sec                                                    | 1.52 sec: 1.10x slower                                                               |
| logging_simple             | 5.72 us                                                     | 6.29 us: 1.10x slower                                                                |
| logging_format             | 6.15 us                                                     | 6.77 us: 1.10x slower                                                                |
| sympy_integrate            | 12.3 ms                                                     | 13.5 ms: 1.10x slower                                                                |
| scimark_lu                 | 54.0 ms                                                     | 59.6 ms: 1.10x slower                                                                |
| pprint_safe_repr           | 493 ms                                                      | 547 ms: 1.11x slower                                                                 |
| generators                 | 19.5 ms                                                     | 21.8 ms: 1.12x slower                                                                |
| xml_etree_process          | 36.5 ms                                                     | 41.0 ms: 1.12x slower                                                                |
| sqlglot_optimize           | 33.1 ms                                                     | 37.1 ms: 1.12x slower                                                                |
| crypto_pyaes               | 42.8 ms                                                     | 48.1 ms: 1.12x slower                                                                |
| float                      | 48.1 ms                                                     | 54.1 ms: 1.13x slower                                                                |
| pprint_pformat             | 991 ms                                                      | 1.12 sec: 1.13x slower                                                               |
| genshi_xml                 | 32.8 ms                                                     | 37.1 ms: 1.13x slower                                                                |
| regex_compile              | 80.1 ms                                                     | 90.8 ms: 1.13x slower                                                                |
| create_gc_cycles           | 829 us                                                      | 939 us: 1.13x slower                                                                 |
| html5lib                   | 38.6 ms                                                     | 43.8 ms: 1.13x slower                                                                |
| async_tree_io_tg           | 512 ms                                                      | 581 ms: 1.13x slower                                                                 |
| async_generators           | 223 ms                                                      | 253 ms: 1.13x slower                                                                 |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.67 ms: 1.14x slower                                                                |
| async_tree_io              | 521 ms                                                      | 594 ms: 1.14x slower                                                                 |
| coroutines                 | 12.5 ms                                                     | 14.3 ms: 1.14x slower                                                                |
| comprehensions             | 10.2 us                                                     | 11.8 us: 1.15x slower                                                                |
| sqlglot_normalize          | 171 ms                                                      | 198 ms: 1.15x slower                                                                 |
| scimark_monte_carlo        | 40.3 ms                                                     | 46.6 ms: 1.16x slower                                                                |
| typing_runtime_protocols   | 100 us                                                      | 116 us: 1.16x slower                                                                 |
| nqueens                    | 55.5 ms                                                     | 64.6 ms: 1.16x slower                                                                |
| pyflate                    | 275 ms                                                      | 321 ms: 1.17x slower                                                                 |
| spectral_norm              | 59.2 ms                                                     | 69.0 ms: 1.17x slower                                                                |
| chaos                      | 37.9 ms                                                     | 44.2 ms: 1.17x slower                                                                |
| genshi_text                | 14.9 ms                                                     | 17.4 ms: 1.17x slower                                                                |
| json_dumps                 | 5.76 ms                                                     | 6.73 ms: 1.17x slower                                                                |
| fannkuch                   | 245 ms                                                      | 286 ms: 1.17x slower                                                                 |
| scimark_fft                | 174 ms                                                      | 204 ms: 1.17x slower                                                                 |
| unpickle_pure_python       | 127 us                                                      | 149 us: 1.17x slower                                                                 |
| sqlglot_parse              | 761 us                                                      | 894 us: 1.17x slower                                                                 |
| sqlglot_transpile          | 952 us                                                      | 1.12 ms: 1.18x slower                                                                |
| pickle_pure_python         | 183 us                                                      | 217 us: 1.19x slower                                                                 |
| hexiom                     | 3.69 ms                                                     | 4.39 ms: 1.19x slower                                                                |
| logging_silent             | 51.0 ns                                                     | 60.8 ns: 1.19x slower                                                                |
| django_template            | 21.8 ms                                                     | 26.3 ms: 1.21x slower                                                                |
| tomli_loads                | 1.36 sec                                                    | 1.65 sec: 1.21x slower                                                               |
| richards                   | 26.0 ms                                                     | 31.7 ms: 1.22x slower                                                                |
| richards_super             | 29.3 ms                                                     | 35.7 ms: 1.22x slower                                                                |
| deltablue                  | 1.86 ms                                                     | 2.28 ms: 1.22x slower                                                                |
| raytrace                   | 156 ms                                                      | 194 ms: 1.25x slower                                                                 |
| scimark_sor                | 72.0 ms                                                     | 90.1 ms: 1.25x slower                                                                |
| nbody                      | 64.5 ms                                                     | 82.9 ms: 1.29x slower                                                                |
| json                       | 2.98 ms                                                     | 4.46 ms: 1.50x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.06x slower                                                                         |

Benchmark hidden because not significant (12): pycparser, asyncio_tcp, async_tree_memoization, bench_thread_pool, gc_traversal, regex_dna, pidigits, deepcopy_reduce, python_startup, async_tree_none_tg, pickle_list, asyncio_tcp_ssl
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown