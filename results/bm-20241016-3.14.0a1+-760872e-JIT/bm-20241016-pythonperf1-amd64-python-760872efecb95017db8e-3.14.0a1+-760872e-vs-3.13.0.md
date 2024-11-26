# Results vs. 3.13.0

- fork: python
- ref: 760872efecb95017db8e
- machine: windows-amd64
- commit hash: 760872e
- commit date: 2024-10-16
- overall geometric mean: 1.008x slower
- HPT reliability: 99.86%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 247 ms: 1.11x slower                                                        |
| docutils       | 1.57 sec                                                    | 1.91 sec: 1.22x slower                                                      |
| html5lib       | 38.9 ms                                                     | 39.7 ms: 1.02x slower                                                       |
| sphinx         | 633 ms                                                      | 767 ms: 1.21x slower                                                        |
| tornado_http   | 93.0 ms                                                     | 98.1 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.12x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 262 ms: 1.10x faster                                                        |
| async_tree_none            | 226 ms                                                      | 234 ms: 1.04x slower                                                        |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 400 ms: 1.06x slower                                                        |
| async_tree_io              | 521 ms                                                      | 554 ms: 1.06x slower                                                        |
| coroutines                 | 12.8 ms                                                     | 13.8 ms: 1.08x slower                                                       |
| async_generators           | 223 ms                                                      | 260 ms: 1.16x slower                                                        |
| async_tree_io_tg           | 518 ms                                                      | 635 ms: 1.23x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                                |

Benchmark hidden because not significant (3): async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 68.4 ms                                                     | 54.7 ms: 1.25x faster                                                       |
| float          | 49.9 ms                                                     | 47.5 ms: 1.05x faster                                                       |
| pidigits       | 148 ms                                                      | 148 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.6 ms: 1.37x faster                                                       |
| regex_effbot   | 1.58 ms                                                     | 1.65 ms: 1.05x slower                                                       |
| regex_dna      | 115 ms                                                      | 123 ms: 1.06x slower                                                        |
| regex_compile  | 80.5 ms                                                     | 91.5 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.39 sec                                                    | 1.27 sec: 1.10x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.2 us: 1.06x faster                                                       |
| xml_etree_generate   | 54.0 ms                                                     | 51.1 ms: 1.06x faster                                                       |
| xml_etree_process    | 37.0 ms                                                     | 36.5 ms: 1.01x faster                                                       |
| xml_etree_iterparse  | 61.8 ms                                                     | 62.9 ms: 1.02x slower                                                       |
| xml_etree_parse      | 93.6 ms                                                     | 95.6 ms: 1.02x slower                                                       |
| pickle_pure_python   | 190 us                                                      | 197 us: 1.04x slower                                                        |
| unpickle_pure_python | 133 us                                                      | 142 us: 1.06x slower                                                        |
| json_dumps           | 5.92 ms                                                     | 6.37 ms: 1.08x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.00x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 23.9 ms: 1.06x faster                                                       |
| python_startup_no_site | 18.1 ms                                                     | 18.4 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.35 ms                                                     | 4.94 ms: 1.29x faster                                                       |
| django_template | 22.4 ms                                                     | 27.0 ms: 1.21x slower                                                       |
| genshi_text     | 15.6 ms                                                     | 19.6 ms: 1.26x slower                                                       |
| genshi_xml      | 35.5 ms                                                     | 46.3 ms: 1.31x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.11x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 513 us: 17.13x faster                                                       |
| deepcopy_memo              | 23.3 us                                                     | 16.4 us: 1.42x faster                                                       |
| regex_v8                   | 21.4 ms                                                     | 15.6 ms: 1.37x faster                                                       |
| mako                       | 6.35 ms                                                     | 4.94 ms: 1.29x faster                                                       |
| nbody                      | 68.4 ms                                                     | 54.7 ms: 1.25x faster                                                       |
| scimark_sor                | 76.2 ms                                                     | 64.0 ms: 1.19x faster                                                       |
| deepcopy                   | 226 us                                                      | 192 us: 1.18x faster                                                        |
| spectral_norm              | 62.8 ms                                                     | 54.5 ms: 1.15x faster                                                       |
| crypto_pyaes               | 45.4 ms                                                     | 39.8 ms: 1.14x faster                                                       |
| scimark_monte_carlo        | 40.8 ms                                                     | 36.1 ms: 1.13x faster                                                       |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.18 ms: 1.13x faster                                                       |
| scimark_fft                | 172 ms                                                      | 154 ms: 1.12x faster                                                        |
| telco                      | 4.79 ms                                                     | 4.34 ms: 1.11x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 262 ms: 1.10x faster                                                        |
| deepcopy_reduce            | 2.06 us                                                     | 1.88 us: 1.10x faster                                                       |
| tomli_loads                | 1.39 sec                                                    | 1.27 sec: 1.10x faster                                                      |
| fannkuch                   | 253 ms                                                      | 231 ms: 1.10x faster                                                        |
| pprint_safe_repr           | 494 ms                                                      | 458 ms: 1.08x faster                                                        |
| pprint_pformat             | 999 ms                                                      | 935 ms: 1.07x faster                                                        |
| json_loads                 | 15.1 us                                                     | 14.2 us: 1.06x faster                                                       |
| python_startup             | 25.4 ms                                                     | 23.9 ms: 1.06x faster                                                       |
| json                       | 3.19 ms                                                     | 3.01 ms: 1.06x faster                                                       |
| xml_etree_generate         | 54.0 ms                                                     | 51.1 ms: 1.06x faster                                                       |
| float                      | 49.9 ms                                                     | 47.5 ms: 1.05x faster                                                       |
| xml_etree_process          | 37.0 ms                                                     | 36.5 ms: 1.01x faster                                                       |
| dulwich_log                | 40.8 ms                                                     | 40.4 ms: 1.01x faster                                                       |
| pidigits                   | 148 ms                                                      | 148 ms: 1.00x slower                                                        |
| python_startup_no_site     | 18.1 ms                                                     | 18.4 ms: 1.01x slower                                                       |
| xml_etree_iterparse        | 61.8 ms                                                     | 62.9 ms: 1.02x slower                                                       |
| pyflate                    | 283 ms                                                      | 289 ms: 1.02x slower                                                        |
| html5lib                   | 38.9 ms                                                     | 39.7 ms: 1.02x slower                                                       |
| xml_etree_parse            | 93.6 ms                                                     | 95.6 ms: 1.02x slower                                                       |
| meteor_contest             | 73.5 ms                                                     | 75.5 ms: 1.03x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 56.5 ns: 1.03x slower                                                       |
| logging_simple             | 5.96 us                                                     | 6.17 us: 1.04x slower                                                       |
| async_tree_none            | 226 ms                                                      | 234 ms: 1.04x slower                                                        |
| pickle_pure_python         | 190 us                                                      | 197 us: 1.04x slower                                                        |
| bench_mp_pool              | 86.4 ms                                                     | 89.8 ms: 1.04x slower                                                       |
| scimark_lu                 | 53.0 ms                                                     | 55.4 ms: 1.04x slower                                                       |
| regex_effbot               | 1.58 ms                                                     | 1.65 ms: 1.05x slower                                                       |
| go                         | 87.0 ms                                                     | 91.2 ms: 1.05x slower                                                       |
| coverage                   | 45.6 ms                                                     | 48.0 ms: 1.05x slower                                                       |
| tornado_http               | 93.0 ms                                                     | 98.1 ms: 1.05x slower                                                       |
| logging_format             | 6.26 us                                                     | 6.62 us: 1.06x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 142 us: 1.06x slower                                                        |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 400 ms: 1.06x slower                                                        |
| async_tree_io              | 521 ms                                                      | 554 ms: 1.06x slower                                                        |
| regex_dna                  | 115 ms                                                      | 123 ms: 1.06x slower                                                        |
| typing_runtime_protocols   | 105 us                                                      | 113 us: 1.07x slower                                                        |
| json_dumps                 | 5.92 ms                                                     | 6.37 ms: 1.08x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 13.8 ms: 1.08x slower                                                       |
| chaos                      | 38.5 ms                                                     | 41.7 ms: 1.08x slower                                                       |
| pycparser                  | 683 ms                                                      | 754 ms: 1.10x slower                                                        |
| comprehensions             | 10.3 us                                                     | 11.4 us: 1.11x slower                                                       |
| 2to3                       | 221 ms                                                      | 247 ms: 1.11x slower                                                        |
| sympy_expand               | 291 ms                                                      | 325 ms: 1.11x slower                                                        |
| create_gc_cycles           | 1.26 ms                                                     | 1.41 ms: 1.12x slower                                                       |
| nqueens                    | 56.7 ms                                                     | 63.5 ms: 1.12x slower                                                       |
| mdp                        | 1.39 sec                                                    | 1.56 sec: 1.12x slower                                                      |
| regex_compile              | 80.5 ms                                                     | 91.5 ms: 1.14x slower                                                       |
| sympy_str                  | 169 ms                                                      | 192 ms: 1.14x slower                                                        |
| async_generators           | 223 ms                                                      | 260 ms: 1.16x slower                                                        |
| sqlglot_parse              | 771 us                                                      | 897 us: 1.16x slower                                                        |
| generators                 | 19.5 ms                                                     | 23.0 ms: 1.18x slower                                                       |
| sqlglot_normalize          | 175 ms                                                      | 207 ms: 1.19x slower                                                        |
| sympy_sum                  | 86.9 ms                                                     | 103 ms: 1.19x slower                                                        |
| django_template            | 22.4 ms                                                     | 27.0 ms: 1.21x slower                                                       |
| sphinx                     | 633 ms                                                      | 767 ms: 1.21x slower                                                        |
| docutils                   | 1.57 sec                                                    | 1.91 sec: 1.22x slower                                                      |
| async_tree_io_tg           | 518 ms                                                      | 635 ms: 1.23x slower                                                        |
| sqlglot_transpile          | 956 us                                                      | 1.18 ms: 1.23x slower                                                       |
| deltablue                  | 1.92 ms                                                     | 2.37 ms: 1.24x slower                                                       |
| richards                   | 27.3 ms                                                     | 34.0 ms: 1.25x slower                                                       |
| richards_super             | 30.9 ms                                                     | 38.5 ms: 1.25x slower                                                       |
| genshi_text                | 15.6 ms                                                     | 19.6 ms: 1.26x slower                                                       |
| sympy_integrate            | 12.5 ms                                                     | 15.8 ms: 1.26x slower                                                       |
| genshi_xml                 | 35.5 ms                                                     | 46.3 ms: 1.31x slower                                                       |
| sqlglot_optimize           | 32.9 ms                                                     | 43.2 ms: 1.31x slower                                                       |
| pylint                     | 211 ms                                                      | 279 ms: 1.32x slower                                                        |
| hexiom                     | 3.89 ms                                                     | 5.21 ms: 1.34x slower                                                       |
| raytrace                   | 160 ms                                                      | 215 ms: 1.35x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (6): bench_thread_pool, pathlib, gc_traversal, async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241016-3.14.0a1+-760872e-JIT/bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.008x slower
# HPT report

- Reliability score: 99.86% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown