# Results vs. 3.13.0

- fork: python
- ref: 5e9e50612eb27aef8f74
- machine: windows-amd64
- commit hash: 5e9e506
- commit date: 2024-10-04
- overall geometric mean: 1.007x slower
- HPT reliability: 99.73%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 253 ms: 1.14x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.95 sec: 1.24x slower                                                     |
| html5lib       | 38.9 ms                                                     | 41.7 ms: 1.07x slower                                                      |
| sphinx         | 633 ms                                                      | 794 ms: 1.25x slower                                                       |
| tornado_http   | 93.0 ms                                                     | 98.2 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                       | 1.15x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 262 ms: 1.10x faster                                                       |
| async_tree_none            | 226 ms                                                      | 217 ms: 1.04x faster                                                       |
| async_tree_none_tg         | 209 ms                                                      | 202 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 401 ms: 1.07x slower                                                       |
| async_tree_io              | 521 ms                                                      | 565 ms: 1.08x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 14.1 ms: 1.11x slower                                                      |
| async_tree_io_tg           | 518 ms                                                      | 574 ms: 1.11x slower                                                       |
| async_generators           | 223 ms                                                      | 260 ms: 1.16x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 68.4 ms                                                     | 49.4 ms: 1.39x faster                                                      |
| float          | 49.9 ms                                                     | 47.2 ms: 1.06x faster                                                      |
| pidigits       | 148 ms                                                      | 147 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 14.8 ms: 1.44x faster                                                      |
| regex_dna      | 115 ms                                                      | 117 ms: 1.02x slower                                                       |
| regex_compile  | 80.5 ms                                                     | 95.7 ms: 1.19x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate   | 54.0 ms                                                     | 50.5 ms: 1.07x faster                                                      |
| tomli_loads          | 1.39 sec                                                    | 1.30 sec: 1.07x faster                                                     |
| json_loads           | 15.1 us                                                     | 14.3 us: 1.06x faster                                                      |
| xml_etree_process    | 37.0 ms                                                     | 36.4 ms: 1.02x faster                                                      |
| json_dumps           | 5.92 ms                                                     | 5.84 ms: 1.01x faster                                                      |
| xml_etree_iterparse  | 61.8 ms                                                     | 63.0 ms: 1.02x slower                                                      |
| xml_etree_parse      | 93.6 ms                                                     | 95.8 ms: 1.02x slower                                                      |
| pickle_pure_python   | 190 us                                                      | 198 us: 1.04x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 147 us: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.00x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 24.3 ms: 1.04x faster                                                      |
| python_startup_no_site | 18.1 ms                                                     | 18.5 ms: 1.02x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.35 ms                                                     | 4.99 ms: 1.27x faster                                                      |
| django_template | 22.4 ms                                                     | 26.9 ms: 1.20x slower                                                      |
| genshi_text     | 15.6 ms                                                     | 19.1 ms: 1.23x slower                                                      |
| genshi_xml      | 35.5 ms                                                     | 47.3 ms: 1.33x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.12x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 523 us: 16.81x faster                                                      |
| regex_v8                   | 21.4 ms                                                     | 14.8 ms: 1.44x faster                                                      |
| deepcopy_memo              | 23.3 us                                                     | 16.2 us: 1.44x faster                                                      |
| nbody                      | 68.4 ms                                                     | 49.4 ms: 1.39x faster                                                      |
| mako                       | 6.35 ms                                                     | 4.99 ms: 1.27x faster                                                      |
| scimark_sor                | 76.2 ms                                                     | 61.9 ms: 1.23x faster                                                      |
| deepcopy                   | 226 us                                                      | 186 us: 1.22x faster                                                       |
| spectral_norm              | 62.8 ms                                                     | 52.6 ms: 1.19x faster                                                      |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.11 ms: 1.17x faster                                                      |
| deepcopy_reduce            | 2.06 us                                                     | 1.81 us: 1.14x faster                                                      |
| scimark_fft                | 172 ms                                                      | 153 ms: 1.13x faster                                                       |
| crypto_pyaes               | 45.4 ms                                                     | 40.6 ms: 1.12x faster                                                      |
| scimark_monte_carlo        | 40.8 ms                                                     | 36.6 ms: 1.11x faster                                                      |
| async_tree_memoization_tg  | 288 ms                                                      | 262 ms: 1.10x faster                                                       |
| pprint_safe_repr           | 494 ms                                                      | 450 ms: 1.10x faster                                                       |
| pprint_pformat             | 999 ms                                                      | 923 ms: 1.08x faster                                                       |
| telco                      | 4.79 ms                                                     | 4.46 ms: 1.08x faster                                                      |
| xml_etree_generate         | 54.0 ms                                                     | 50.5 ms: 1.07x faster                                                      |
| tomli_loads                | 1.39 sec                                                    | 1.30 sec: 1.07x faster                                                     |
| float                      | 49.9 ms                                                     | 47.2 ms: 1.06x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.3 us: 1.06x faster                                                      |
| python_startup             | 25.4 ms                                                     | 24.3 ms: 1.04x faster                                                      |
| async_tree_none            | 226 ms                                                      | 217 ms: 1.04x faster                                                       |
| async_tree_none_tg         | 209 ms                                                      | 202 ms: 1.04x faster                                                       |
| gc_traversal               | 1.97 ms                                                     | 1.93 ms: 1.02x faster                                                      |
| xml_etree_process          | 37.0 ms                                                     | 36.4 ms: 1.02x faster                                                      |
| json_dumps                 | 5.92 ms                                                     | 5.84 ms: 1.01x faster                                                      |
| pidigits                   | 148 ms                                                      | 147 ms: 1.01x faster                                                       |
| xml_etree_iterparse        | 61.8 ms                                                     | 63.0 ms: 1.02x slower                                                      |
| regex_dna                  | 115 ms                                                      | 117 ms: 1.02x slower                                                       |
| python_startup_no_site     | 18.1 ms                                                     | 18.5 ms: 1.02x slower                                                      |
| xml_etree_parse            | 93.6 ms                                                     | 95.8 ms: 1.02x slower                                                      |
| meteor_contest             | 73.5 ms                                                     | 75.4 ms: 1.02x slower                                                      |
| bench_mp_pool              | 86.4 ms                                                     | 88.9 ms: 1.03x slower                                                      |
| logging_simple             | 5.96 us                                                     | 6.15 us: 1.03x slower                                                      |
| pickle_pure_python         | 190 us                                                      | 198 us: 1.04x slower                                                       |
| typing_runtime_protocols   | 105 us                                                      | 111 us: 1.05x slower                                                       |
| scimark_lu                 | 53.0 ms                                                     | 55.7 ms: 1.05x slower                                                      |
| tornado_http               | 93.0 ms                                                     | 98.2 ms: 1.06x slower                                                      |
| go                         | 87.0 ms                                                     | 91.9 ms: 1.06x slower                                                      |
| dulwich_log                | 40.8 ms                                                     | 43.2 ms: 1.06x slower                                                      |
| logging_format             | 6.26 us                                                     | 6.63 us: 1.06x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 58.2 ns: 1.07x slower                                                      |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 401 ms: 1.07x slower                                                       |
| html5lib                   | 38.9 ms                                                     | 41.7 ms: 1.07x slower                                                      |
| chaos                      | 38.5 ms                                                     | 41.5 ms: 1.08x slower                                                      |
| async_tree_io              | 521 ms                                                      | 565 ms: 1.08x slower                                                       |
| coverage                   | 45.6 ms                                                     | 49.6 ms: 1.09x slower                                                      |
| pyflate                    | 283 ms                                                      | 310 ms: 1.09x slower                                                       |
| create_gc_cycles           | 1.26 ms                                                     | 1.38 ms: 1.10x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 147 us: 1.10x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 14.1 ms: 1.11x slower                                                      |
| async_tree_io_tg           | 518 ms                                                      | 574 ms: 1.11x slower                                                       |
| pycparser                  | 683 ms                                                      | 759 ms: 1.11x slower                                                       |
| comprehensions             | 10.3 us                                                     | 11.6 us: 1.13x slower                                                      |
| 2to3                       | 221 ms                                                      | 253 ms: 1.14x slower                                                       |
| sympy_expand               | 291 ms                                                      | 334 ms: 1.15x slower                                                       |
| nqueens                    | 56.7 ms                                                     | 65.1 ms: 1.15x slower                                                      |
| sqlglot_parse              | 771 us                                                      | 887 us: 1.15x slower                                                       |
| mdp                        | 1.39 sec                                                    | 1.61 sec: 1.16x slower                                                     |
| sympy_str                  | 169 ms                                                      | 196 ms: 1.16x slower                                                       |
| async_generators           | 223 ms                                                      | 260 ms: 1.16x slower                                                       |
| sqlglot_normalize          | 175 ms                                                      | 205 ms: 1.17x slower                                                       |
| regex_compile              | 80.5 ms                                                     | 95.7 ms: 1.19x slower                                                      |
| generators                 | 19.5 ms                                                     | 23.2 ms: 1.19x slower                                                      |
| sympy_sum                  | 86.9 ms                                                     | 104 ms: 1.20x slower                                                       |
| django_template            | 22.4 ms                                                     | 26.9 ms: 1.20x slower                                                      |
| deltablue                  | 1.92 ms                                                     | 2.34 ms: 1.22x slower                                                      |
| sqlglot_transpile          | 956 us                                                      | 1.17 ms: 1.23x slower                                                      |
| genshi_text                | 15.6 ms                                                     | 19.1 ms: 1.23x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.95 sec: 1.24x slower                                                     |
| sympy_integrate            | 12.5 ms                                                     | 15.6 ms: 1.25x slower                                                      |
| richards_super             | 30.9 ms                                                     | 38.6 ms: 1.25x slower                                                      |
| sphinx                     | 633 ms                                                      | 794 ms: 1.25x slower                                                       |
| richards                   | 27.3 ms                                                     | 34.5 ms: 1.26x slower                                                      |
| raytrace                   | 160 ms                                                      | 202 ms: 1.27x slower                                                       |
| sqlglot_optimize           | 32.9 ms                                                     | 42.9 ms: 1.30x slower                                                      |
| pylint                     | 211 ms                                                      | 279 ms: 1.33x slower                                                       |
| genshi_xml                 | 35.5 ms                                                     | 47.3 ms: 1.33x slower                                                      |
| hexiom                     | 3.89 ms                                                     | 5.28 ms: 1.36x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (7): json, bench_thread_pool, fannkuch, regex_effbot, async_tree_cpu_io_mixed, pathlib, async_tree_memoization
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241004-3.14.0a0-5e9e506-JIT/bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.007x slower
# HPT report

- Reliability score: 99.73% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown