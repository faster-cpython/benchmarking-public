# Results vs. 3.13.0

- fork: python
- ref: ded105a62b9d78717f8d
- machine: windows-amd64
- commit hash: ded105a
- commit date: 2024-10-21
- overall geometric mean: 1.03x slower
- HPT reliability: 99.72%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 246 ms: 1.14x slower                                                        |
| docutils       | 1.57 sec                                                    | 1.91 sec: 1.21x slower                                                      |
| html5lib       | 38.6 ms                                                     | 39.5 ms: 1.02x slower                                                       |
| tornado_http   | 92.8 ms                                                     | 96.2 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.10x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 259 ms: 1.11x faster                                                        |
| async_tree_none            | 223 ms                                                      | 217 ms: 1.03x faster                                                        |
| async_tree_none_tg         | 206 ms                                                      | 209 ms: 1.01x slower                                                        |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 400 ms: 1.07x slower                                                        |
| async_tree_io              | 521 ms                                                      | 559 ms: 1.07x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                                       |
| async_generators           | 223 ms                                                      | 258 ms: 1.16x slower                                                        |
| async_tree_io_tg           | 512 ms                                                      | 635 ms: 1.24x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                                |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 64.5 ms                                                     | 52.8 ms: 1.22x faster                                                       |
| float          | 48.1 ms                                                     | 47.5 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                       |
| regex_v8       | 14.7 ms                                                     | 15.1 ms: 1.03x slower                                                       |
| regex_dna      | 114 ms                                                      | 123 ms: 1.08x slower                                                        |
| regex_compile  | 80.1 ms                                                     | 91.1 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                                    | 1.26 sec: 1.08x faster                                                      |
| xml_etree_generate   | 53.3 ms                                                     | 50.3 ms: 1.06x faster                                                       |
| xml_etree_process    | 36.5 ms                                                     | 36.1 ms: 1.01x faster                                                       |
| xml_etree_iterparse  | 62.3 ms                                                     | 61.6 ms: 1.01x faster                                                       |
| json_loads           | 14.3 us                                                     | 14.6 us: 1.02x slower                                                       |
| pickle_pure_python   | 183 us                                                      | 199 us: 1.09x slower                                                        |
| json_dumps           | 5.76 ms                                                     | 6.30 ms: 1.09x slower                                                       |
| unpickle_pure_python | 127 us                                                      | 143 us: 1.12x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 17.8 ms                                                     | 18.8 ms: 1.06x slower                                                       |
| python_startup         | 22.2 ms                                                     | 24.3 ms: 1.09x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 4.99 ms: 1.25x faster                                                       |
| django_template | 21.8 ms                                                     | 27.6 ms: 1.27x slower                                                       |
| genshi_text     | 14.9 ms                                                     | 18.9 ms: 1.27x slower                                                       |
| genshi_xml      | 32.8 ms                                                     | 44.1 ms: 1.35x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.15x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 523 us: 16.60x faster                                                       |
| deepcopy_memo              | 21.8 us                                                     | 16.6 us: 1.31x faster                                                       |
| mako                       | 6.24 ms                                                     | 4.99 ms: 1.25x faster                                                       |
| nbody                      | 64.5 ms                                                     | 52.8 ms: 1.22x faster                                                       |
| deepcopy                   | 223 us                                                      | 190 us: 1.18x faster                                                        |
| scimark_sor                | 72.0 ms                                                     | 64.3 ms: 1.12x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 259 ms: 1.11x faster                                                        |
| spectral_norm              | 59.2 ms                                                     | 54.0 ms: 1.10x faster                                                       |
| scimark_fft                | 174 ms                                                      | 159 ms: 1.10x faster                                                        |
| scimark_monte_carlo        | 40.3 ms                                                     | 36.8 ms: 1.09x faster                                                       |
| pprint_safe_repr           | 493 ms                                                      | 450 ms: 1.09x faster                                                        |
| deepcopy_reduce            | 2.02 us                                                     | 1.85 us: 1.09x faster                                                       |
| tomli_loads                | 1.36 sec                                                    | 1.26 sec: 1.08x faster                                                      |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.19 ms: 1.07x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.56 ms: 1.06x faster                                                       |
| xml_etree_generate         | 53.3 ms                                                     | 50.3 ms: 1.06x faster                                                       |
| crypto_pyaes               | 42.8 ms                                                     | 40.6 ms: 1.05x faster                                                       |
| fannkuch                   | 245 ms                                                      | 232 ms: 1.05x faster                                                        |
| pprint_pformat             | 991 ms                                                      | 953 ms: 1.04x faster                                                        |
| async_tree_none            | 223 ms                                                      | 217 ms: 1.03x faster                                                        |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                       |
| scimark_lu                 | 54.0 ms                                                     | 53.3 ms: 1.01x faster                                                       |
| float                      | 48.1 ms                                                     | 47.5 ms: 1.01x faster                                                       |
| xml_etree_process          | 36.5 ms                                                     | 36.1 ms: 1.01x faster                                                       |
| xml_etree_iterparse        | 62.3 ms                                                     | 61.6 ms: 1.01x faster                                                       |
| pathlib                    | 81.2 ms                                                     | 80.4 ms: 1.01x faster                                                       |
| async_tree_none_tg         | 206 ms                                                      | 209 ms: 1.01x slower                                                        |
| dulwich_log                | 40.4 ms                                                     | 41.0 ms: 1.02x slower                                                       |
| json_loads                 | 14.3 us                                                     | 14.6 us: 1.02x slower                                                       |
| html5lib                   | 38.6 ms                                                     | 39.5 ms: 1.02x slower                                                       |
| regex_v8                   | 14.7 ms                                                     | 15.1 ms: 1.03x slower                                                       |
| pyflate                    | 275 ms                                                      | 285 ms: 1.03x slower                                                        |
| json                       | 2.98 ms                                                     | 3.09 ms: 1.03x slower                                                       |
| tornado_http               | 92.8 ms                                                     | 96.2 ms: 1.04x slower                                                       |
| meteor_contest             | 72.3 ms                                                     | 75.4 ms: 1.04x slower                                                       |
| logging_format             | 6.15 us                                                     | 6.49 us: 1.06x slower                                                       |
| python_startup_no_site     | 17.8 ms                                                     | 18.8 ms: 1.06x slower                                                       |
| go                         | 84.6 ms                                                     | 90.4 ms: 1.07x slower                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 400 ms: 1.07x slower                                                        |
| async_tree_io              | 521 ms                                                      | 559 ms: 1.07x slower                                                        |
| logging_simple             | 5.72 us                                                     | 6.15 us: 1.07x slower                                                       |
| coverage                   | 46.7 ms                                                     | 50.3 ms: 1.08x slower                                                       |
| regex_dna                  | 114 ms                                                      | 123 ms: 1.08x slower                                                        |
| pickle_pure_python         | 183 us                                                      | 199 us: 1.09x slower                                                        |
| chaos                      | 37.9 ms                                                     | 41.2 ms: 1.09x slower                                                       |
| python_startup             | 22.2 ms                                                     | 24.3 ms: 1.09x slower                                                       |
| json_dumps                 | 5.76 ms                                                     | 6.30 ms: 1.09x slower                                                       |
| typing_runtime_protocols   | 100 us                                                      | 111 us: 1.10x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                                       |
| logging_silent             | 51.0 ns                                                     | 56.3 ns: 1.10x slower                                                       |
| mdp                        | 1.38 sec                                                    | 1.54 sec: 1.11x slower                                                      |
| nqueens                    | 55.5 ms                                                     | 61.9 ms: 1.12x slower                                                       |
| unpickle_pure_python       | 127 us                                                      | 143 us: 1.12x slower                                                        |
| comprehensions             | 10.2 us                                                     | 11.6 us: 1.13x slower                                                       |
| sympy_expand               | 285 ms                                                      | 323 ms: 1.13x slower                                                        |
| 2to3                       | 217 ms                                                      | 246 ms: 1.14x slower                                                        |
| regex_compile              | 80.1 ms                                                     | 91.1 ms: 1.14x slower                                                       |
| sympy_str                  | 166 ms                                                      | 192 ms: 1.16x slower                                                        |
| async_generators           | 223 ms                                                      | 258 ms: 1.16x slower                                                        |
| generators                 | 19.5 ms                                                     | 22.7 ms: 1.17x slower                                                       |
| sqlglot_parse              | 761 us                                                      | 893 us: 1.17x slower                                                        |
| sympy_sum                  | 86.4 ms                                                     | 102 ms: 1.18x slower                                                        |
| sqlglot_normalize          | 171 ms                                                      | 206 ms: 1.21x slower                                                        |
| docutils                   | 1.57 sec                                                    | 1.91 sec: 1.21x slower                                                      |
| sqlglot_transpile          | 952 us                                                      | 1.17 ms: 1.23x slower                                                       |
| deltablue                  | 1.86 ms                                                     | 2.31 ms: 1.24x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 635 ms: 1.24x slower                                                        |
| gc_traversal               | 1.55 ms                                                     | 1.96 ms: 1.26x slower                                                       |
| django_template            | 21.8 ms                                                     | 27.6 ms: 1.27x slower                                                       |
| genshi_text                | 14.9 ms                                                     | 18.9 ms: 1.27x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 15.7 ms: 1.28x slower                                                       |
| bench_mp_pool              | 69.6 ms                                                     | 89.2 ms: 1.28x slower                                                       |
| sqlglot_optimize           | 33.1 ms                                                     | 42.6 ms: 1.29x slower                                                       |
| richards                   | 26.0 ms                                                     | 34.0 ms: 1.31x slower                                                       |
| richards_super             | 29.3 ms                                                     | 38.3 ms: 1.31x slower                                                       |
| pylint                     | 211 ms                                                      | 281 ms: 1.33x slower                                                        |
| genshi_xml                 | 32.8 ms                                                     | 44.1 ms: 1.35x slower                                                       |
| raytrace                   | 156 ms                                                      | 212 ms: 1.35x slower                                                        |
| hexiom                     | 3.69 ms                                                     | 5.13 ms: 1.39x slower                                                       |
| create_gc_cycles           | 829 us                                                      | 1.40 ms: 1.69x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                                |

Benchmark hidden because not significant (6): pycparser, async_tree_cpu_io_mixed, xml_etree_parse, pidigits, bench_thread_pool, async_tree_memoization
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20241021-3.14.0a1+-ded105a-JIT/bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a.json: sphinx

# HPT report

- Reliability score: 99.72% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown