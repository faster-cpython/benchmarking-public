# Results vs. 3.13.0

- fork: python
- ref: 99400930ac1d4e5e10a5
- machine: windows-amd64
- commit hash: 9940093
- commit date: 2024-10-09
- overall geometric mean: 1.048x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 227 ms: 1.03x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.73 sec: 1.10x slower                                                     |
| html5lib       | 38.9 ms                                                     | 41.9 ms: 1.08x slower                                                      |
| tornado_http   | 93.0 ms                                                     | 94.1 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 268 ms: 1.07x faster                                                       |
| async_tree_none            | 226 ms                                                      | 219 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 395 ms: 1.05x slower                                                       |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 404 ms: 1.05x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 13.9 ms: 1.09x slower                                                      |
| async_generators           | 223 ms                                                      | 248 ms: 1.11x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 593 ms: 1.14x slower                                                       |
| async_tree_io              | 521 ms                                                      | 603 ms: 1.16x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 149 ms: 1.01x slower                                                       |
| float          | 49.9 ms                                                     | 56.5 ms: 1.13x slower                                                      |
| nbody          | 68.4 ms                                                     | 85.6 ms: 1.25x slower                                                      |
| Geometric mean | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 16.2 ms: 1.32x faster                                                      |
| regex_dna      | 115 ms                                                      | 114 ms: 1.01x faster                                                       |
| regex_compile  | 80.5 ms                                                     | 91.8 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 93.6 ms                                                     | 95.9 ms: 1.03x slower                                                      |
| xml_etree_iterparse  | 61.8 ms                                                     | 66.0 ms: 1.07x slower                                                      |
| json_dumps           | 5.92 ms                                                     | 6.41 ms: 1.08x slower                                                      |
| xml_etree_generate   | 54.0 ms                                                     | 59.4 ms: 1.10x slower                                                      |
| xml_etree_process    | 37.0 ms                                                     | 42.5 ms: 1.15x slower                                                      |
| pickle_pure_python   | 190 us                                                      | 220 us: 1.16x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 159 us: 1.19x slower                                                       |
| tomli_loads          | 1.39 sec                                                    | 1.66 sec: 1.19x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.10x slower                                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 22.1 ms: 1.15x faster                                                      |
| python_startup_no_site | 18.1 ms                                                     | 17.7 ms: 1.02x faster                                                      |
| Geometric mean         | (ref)                                                       | 1.08x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 35.5 ms                                                     | 38.3 ms: 1.08x slower                                                      |
| mako            | 6.35 ms                                                     | 7.19 ms: 1.13x slower                                                      |
| genshi_text     | 15.6 ms                                                     | 17.8 ms: 1.14x slower                                                      |
| django_template | 22.4 ms                                                     | 26.3 ms: 1.18x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.13x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 528 us: 16.66x faster                                                      |
| create_gc_cycles           | 1.26 ms                                                     | 928 us: 1.36x faster                                                       |
| regex_v8                   | 21.4 ms                                                     | 16.2 ms: 1.32x faster                                                      |
| gc_traversal               | 1.97 ms                                                     | 1.53 ms: 1.28x faster                                                      |
| bench_mp_pool              | 86.4 ms                                                     | 69.2 ms: 1.25x faster                                                      |
| deepcopy                   | 226 us                                                      | 193 us: 1.17x faster                                                       |
| python_startup             | 25.4 ms                                                     | 22.1 ms: 1.15x faster                                                      |
| deepcopy_memo              | 23.3 us                                                     | 21.6 us: 1.08x faster                                                      |
| async_tree_memoization_tg  | 288 ms                                                      | 268 ms: 1.07x faster                                                       |
| async_tree_none            | 226 ms                                                      | 219 ms: 1.03x faster                                                       |
| deepcopy_reduce            | 2.06 us                                                     | 1.99 us: 1.03x faster                                                      |
| python_startup_no_site     | 18.1 ms                                                     | 17.7 ms: 1.02x faster                                                      |
| regex_dna                  | 115 ms                                                      | 114 ms: 1.01x faster                                                       |
| pidigits                   | 148 ms                                                      | 149 ms: 1.01x slower                                                       |
| tornado_http               | 93.0 ms                                                     | 94.1 ms: 1.01x slower                                                      |
| telco                      | 4.79 ms                                                     | 4.90 ms: 1.02x slower                                                      |
| xml_etree_parse            | 93.6 ms                                                     | 95.9 ms: 1.03x slower                                                      |
| 2to3                       | 221 ms                                                      | 227 ms: 1.03x slower                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 395 ms: 1.05x slower                                                       |
| sympy_sum                  | 86.9 ms                                                     | 91.5 ms: 1.05x slower                                                      |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 404 ms: 1.05x slower                                                       |
| go                         | 87.0 ms                                                     | 91.7 ms: 1.05x slower                                                      |
| mdp                        | 1.39 sec                                                    | 1.47 sec: 1.06x slower                                                     |
| meteor_contest             | 73.5 ms                                                     | 78.1 ms: 1.06x slower                                                      |
| sympy_str                  | 169 ms                                                      | 179 ms: 1.06x slower                                                       |
| xml_etree_iterparse        | 61.8 ms                                                     | 66.0 ms: 1.07x slower                                                      |
| coverage                   | 45.6 ms                                                     | 48.7 ms: 1.07x slower                                                      |
| sympy_expand               | 291 ms                                                      | 312 ms: 1.07x slower                                                       |
| html5lib                   | 38.9 ms                                                     | 41.9 ms: 1.08x slower                                                      |
| typing_runtime_protocols   | 105 us                                                      | 114 us: 1.08x slower                                                       |
| genshi_xml                 | 35.5 ms                                                     | 38.3 ms: 1.08x slower                                                      |
| dulwich_log                | 40.8 ms                                                     | 44.2 ms: 1.08x slower                                                      |
| json_dumps                 | 5.92 ms                                                     | 6.41 ms: 1.08x slower                                                      |
| pylint                     | 211 ms                                                      | 230 ms: 1.09x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 13.9 ms: 1.09x slower                                                      |
| sympy_integrate            | 12.5 ms                                                     | 13.7 ms: 1.09x slower                                                      |
| pycparser                  | 683 ms                                                      | 749 ms: 1.10x slower                                                       |
| xml_etree_generate         | 54.0 ms                                                     | 59.4 ms: 1.10x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.73 sec: 1.10x slower                                                     |
| crypto_pyaes               | 45.4 ms                                                     | 50.1 ms: 1.10x slower                                                      |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.72 ms: 1.11x slower                                                      |
| async_generators           | 223 ms                                                      | 248 ms: 1.11x slower                                                       |
| logging_simple             | 5.96 us                                                     | 6.62 us: 1.11x slower                                                      |
| logging_format             | 6.26 us                                                     | 7.02 us: 1.12x slower                                                      |
| float                      | 49.9 ms                                                     | 56.5 ms: 1.13x slower                                                      |
| generators                 | 19.5 ms                                                     | 22.1 ms: 1.13x slower                                                      |
| mako                       | 6.35 ms                                                     | 7.19 ms: 1.13x slower                                                      |
| regex_compile              | 80.5 ms                                                     | 91.8 ms: 1.14x slower                                                      |
| genshi_text                | 15.6 ms                                                     | 17.8 ms: 1.14x slower                                                      |
| sqlglot_normalize          | 175 ms                                                      | 200 ms: 1.14x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 593 ms: 1.14x slower                                                       |
| xml_etree_process          | 37.0 ms                                                     | 42.5 ms: 1.15x slower                                                      |
| sqlglot_optimize           | 32.9 ms                                                     | 37.9 ms: 1.15x slower                                                      |
| nqueens                    | 56.7 ms                                                     | 65.5 ms: 1.16x slower                                                      |
| async_tree_io              | 521 ms                                                      | 603 ms: 1.16x slower                                                       |
| hexiom                     | 3.89 ms                                                     | 4.52 ms: 1.16x slower                                                      |
| pickle_pure_python         | 190 us                                                      | 220 us: 1.16x slower                                                       |
| pprint_safe_repr           | 494 ms                                                      | 575 ms: 1.17x slower                                                       |
| comprehensions             | 10.3 us                                                     | 12.0 us: 1.17x slower                                                      |
| fannkuch                   | 253 ms                                                      | 297 ms: 1.17x slower                                                       |
| pyflate                    | 283 ms                                                      | 332 ms: 1.17x slower                                                       |
| django_template            | 22.4 ms                                                     | 26.3 ms: 1.18x slower                                                      |
| pprint_pformat             | 999 ms                                                      | 1.18 sec: 1.18x slower                                                     |
| chaos                      | 38.5 ms                                                     | 45.5 ms: 1.18x slower                                                      |
| spectral_norm              | 62.8 ms                                                     | 74.6 ms: 1.19x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 159 us: 1.19x slower                                                       |
| tomli_loads                | 1.39 sec                                                    | 1.66 sec: 1.19x slower                                                     |
| logging_silent             | 54.6 ns                                                     | 65.4 ns: 1.20x slower                                                      |
| sqlglot_transpile          | 956 us                                                      | 1.15 ms: 1.20x slower                                                      |
| sqlglot_parse              | 771 us                                                      | 936 us: 1.21x slower                                                       |
| deltablue                  | 1.92 ms                                                     | 2.33 ms: 1.22x slower                                                      |
| richards                   | 27.3 ms                                                     | 33.7 ms: 1.23x slower                                                      |
| richards_super             | 30.9 ms                                                     | 38.1 ms: 1.23x slower                                                      |
| scimark_lu                 | 53.0 ms                                                     | 65.3 ms: 1.23x slower                                                      |
| scimark_monte_carlo        | 40.8 ms                                                     | 50.4 ms: 1.24x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 94.8 ms: 1.24x slower                                                      |
| scimark_fft                | 172 ms                                                      | 215 ms: 1.25x slower                                                       |
| nbody                      | 68.4 ms                                                     | 85.6 ms: 1.25x slower                                                      |
| raytrace                   | 160 ms                                                      | 201 ms: 1.26x slower                                                       |
| json                       | 3.19 ms                                                     | 4.52 ms: 1.42x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (6): async_tree_memoization, json_loads, bench_thread_pool, pathlib, regex_effbot, async_tree_none_tg
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241009-3.14.0a0-9940093/bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.048x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown