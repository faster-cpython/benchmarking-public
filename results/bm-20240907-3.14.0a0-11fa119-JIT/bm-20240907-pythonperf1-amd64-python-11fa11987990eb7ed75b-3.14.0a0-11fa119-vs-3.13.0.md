# Results vs. 3.13.0

- fork: python
- ref: 11fa11987990eb7ed75b
- machine: windows-amd64
- commit hash: 11fa119
- commit date: 2024-09-07
- overall geometric mean: 1.029x faster
- HPT reliability: 98.90%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 241 ms: 1.09x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.91 sec: 1.22x slower                                                     |
| html5lib       | 38.9 ms                                                     | 42.0 ms: 1.08x slower                                                      |
| tornado_http   | 93.0 ms                                                     | 97.7 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 254 ms: 1.13x faster                                                       |
| async_tree_none            | 226 ms                                                      | 201 ms: 1.12x faster                                                       |
| async_tree_none_tg         | 209 ms                                                      | 195 ms: 1.07x faster                                                       |
| async_tree_memoization     | 276 ms                                                      | 258 ms: 1.07x faster                                                       |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 393 ms: 1.03x slower                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 393 ms: 1.04x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 555 ms: 1.07x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 13.8 ms: 1.08x slower                                                      |
| async_tree_io              | 521 ms                                                      | 584 ms: 1.12x slower                                                       |
| async_generators           | 223 ms                                                      | 264 ms: 1.18x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 68.4 ms                                                     | 49.0 ms: 1.40x faster                                                      |
| float          | 49.9 ms                                                     | 43.8 ms: 1.14x faster                                                      |
| pidigits       | 148 ms                                                      | 150 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.2 ms: 1.41x faster                                                      |
| regex_effbot   | 1.58 ms                                                     | 1.62 ms: 1.03x slower                                                      |
| regex_dna      | 115 ms                                                      | 124 ms: 1.07x slower                                                       |
| regex_compile  | 80.5 ms                                                     | 95.2 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.39 sec                                                    | 1.24 sec: 1.12x faster                                                     |
| xml_etree_generate   | 54.0 ms                                                     | 49.0 ms: 1.10x faster                                                      |
| xml_etree_process    | 37.0 ms                                                     | 34.7 ms: 1.07x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.3 us: 1.06x faster                                                      |
| xml_etree_parse      | 93.6 ms                                                     | 92.6 ms: 1.01x faster                                                      |
| json_dumps           | 5.92 ms                                                     | 5.86 ms: 1.01x faster                                                      |
| pickle_pure_python   | 190 us                                                      | 194 us: 1.02x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 141 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 22.3 ms: 1.14x faster                                                      |
| python_startup_no_site | 18.1 ms                                                     | 18.5 ms: 1.02x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.35 ms                                                     | 5.15 ms: 1.23x faster                                                      |
| django_template | 22.4 ms                                                     | 26.1 ms: 1.17x slower                                                      |
| genshi_text     | 15.6 ms                                                     | 18.7 ms: 1.20x slower                                                      |
| genshi_xml      | 35.5 ms                                                     | 44.0 ms: 1.24x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.09x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 520 us: 16.92x faster                                                      |
| deepcopy_memo              | 23.3 us                                                     | 15.2 us: 1.53x faster                                                      |
| regex_v8                   | 21.4 ms                                                     | 15.2 ms: 1.41x faster                                                      |
| nbody                      | 68.4 ms                                                     | 49.0 ms: 1.40x faster                                                      |
| spectral_norm              | 62.8 ms                                                     | 45.6 ms: 1.38x faster                                                      |
| create_gc_cycles           | 1.26 ms                                                     | 914 us: 1.38x faster                                                       |
| scimark_sor                | 76.2 ms                                                     | 59.9 ms: 1.27x faster                                                      |
| gc_traversal               | 1.97 ms                                                     | 1.56 ms: 1.26x faster                                                      |
| mako                       | 6.35 ms                                                     | 5.15 ms: 1.23x faster                                                      |
| bench_mp_pool              | 86.4 ms                                                     | 71.6 ms: 1.21x faster                                                      |
| deepcopy                   | 226 us                                                      | 188 us: 1.20x faster                                                       |
| crypto_pyaes               | 45.4 ms                                                     | 38.3 ms: 1.19x faster                                                      |
| scimark_fft                | 172 ms                                                      | 148 ms: 1.17x faster                                                       |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.12 ms: 1.16x faster                                                      |
| deepcopy_reduce            | 2.06 us                                                     | 1.80 us: 1.14x faster                                                      |
| python_startup             | 25.4 ms                                                     | 22.3 ms: 1.14x faster                                                      |
| float                      | 49.9 ms                                                     | 43.8 ms: 1.14x faster                                                      |
| async_tree_memoization_tg  | 288 ms                                                      | 254 ms: 1.13x faster                                                       |
| async_tree_none            | 226 ms                                                      | 201 ms: 1.12x faster                                                       |
| tomli_loads                | 1.39 sec                                                    | 1.24 sec: 1.12x faster                                                     |
| xml_etree_generate         | 54.0 ms                                                     | 49.0 ms: 1.10x faster                                                      |
| fannkuch                   | 253 ms                                                      | 232 ms: 1.09x faster                                                       |
| pyflate                    | 283 ms                                                      | 261 ms: 1.09x faster                                                       |
| json                       | 3.19 ms                                                     | 2.97 ms: 1.07x faster                                                      |
| xml_etree_process          | 37.0 ms                                                     | 34.7 ms: 1.07x faster                                                      |
| async_tree_none_tg         | 209 ms                                                      | 195 ms: 1.07x faster                                                       |
| async_tree_memoization     | 276 ms                                                      | 258 ms: 1.07x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.3 us: 1.06x faster                                                      |
| deltablue                  | 1.92 ms                                                     | 1.83 ms: 1.05x faster                                                      |
| telco                      | 4.79 ms                                                     | 4.64 ms: 1.03x faster                                                      |
| pathlib                    | 80.9 ms                                                     | 79.5 ms: 1.02x faster                                                      |
| scimark_lu                 | 53.0 ms                                                     | 52.3 ms: 1.01x faster                                                      |
| xml_etree_parse            | 93.6 ms                                                     | 92.6 ms: 1.01x faster                                                      |
| json_dumps                 | 5.92 ms                                                     | 5.86 ms: 1.01x faster                                                      |
| pprint_safe_repr           | 494 ms                                                      | 503 ms: 1.02x slower                                                       |
| pidigits                   | 148 ms                                                      | 150 ms: 1.02x slower                                                       |
| python_startup_no_site     | 18.1 ms                                                     | 18.5 ms: 1.02x slower                                                      |
| pickle_pure_python         | 190 us                                                      | 194 us: 1.02x slower                                                       |
| meteor_contest             | 73.5 ms                                                     | 75.1 ms: 1.02x slower                                                      |
| regex_effbot               | 1.58 ms                                                     | 1.62 ms: 1.03x slower                                                      |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 393 ms: 1.03x slower                                                       |
| logging_format             | 6.26 us                                                     | 6.43 us: 1.03x slower                                                      |
| typing_runtime_protocols   | 105 us                                                      | 108 us: 1.03x slower                                                       |
| comprehensions             | 10.3 us                                                     | 10.6 us: 1.03x slower                                                      |
| scimark_monte_carlo        | 40.8 ms                                                     | 42.1 ms: 1.03x slower                                                      |
| pprint_pformat             | 999 ms                                                      | 1.03 sec: 1.03x slower                                                     |
| pycparser                  | 683 ms                                                      | 706 ms: 1.03x slower                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 393 ms: 1.04x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 57.3 ns: 1.05x slower                                                      |
| go                         | 87.0 ms                                                     | 91.4 ms: 1.05x slower                                                      |
| tornado_http               | 93.0 ms                                                     | 97.7 ms: 1.05x slower                                                      |
| dulwich_log                | 40.8 ms                                                     | 43.0 ms: 1.05x slower                                                      |
| chaos                      | 38.5 ms                                                     | 40.6 ms: 1.05x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 141 us: 1.06x slower                                                       |
| coverage                   | 45.6 ms                                                     | 48.2 ms: 1.06x slower                                                      |
| nqueens                    | 56.7 ms                                                     | 60.5 ms: 1.07x slower                                                      |
| async_tree_io_tg           | 518 ms                                                      | 555 ms: 1.07x slower                                                       |
| regex_dna                  | 115 ms                                                      | 124 ms: 1.07x slower                                                       |
| mdp                        | 1.39 sec                                                    | 1.49 sec: 1.08x slower                                                     |
| html5lib                   | 38.9 ms                                                     | 42.0 ms: 1.08x slower                                                      |
| coroutines                 | 12.8 ms                                                     | 13.8 ms: 1.08x slower                                                      |
| 2to3                       | 221 ms                                                      | 241 ms: 1.09x slower                                                       |
| sympy_str                  | 169 ms                                                      | 188 ms: 1.12x slower                                                       |
| async_tree_io              | 521 ms                                                      | 584 ms: 1.12x slower                                                       |
| sympy_sum                  | 86.9 ms                                                     | 97.8 ms: 1.13x slower                                                      |
| sympy_expand               | 291 ms                                                      | 329 ms: 1.13x slower                                                       |
| sqlglot_normalize          | 175 ms                                                      | 200 ms: 1.14x slower                                                       |
| sqlglot_parse              | 771 us                                                      | 883 us: 1.15x slower                                                       |
| django_template            | 22.4 ms                                                     | 26.1 ms: 1.17x slower                                                      |
| generators                 | 19.5 ms                                                     | 22.8 ms: 1.17x slower                                                      |
| sympy_integrate            | 12.5 ms                                                     | 14.8 ms: 1.18x slower                                                      |
| async_generators           | 223 ms                                                      | 264 ms: 1.18x slower                                                       |
| regex_compile              | 80.5 ms                                                     | 95.2 ms: 1.18x slower                                                      |
| genshi_text                | 15.6 ms                                                     | 18.7 ms: 1.20x slower                                                      |
| sqlglot_transpile          | 956 us                                                      | 1.15 ms: 1.20x slower                                                      |
| sqlglot_optimize           | 32.9 ms                                                     | 39.8 ms: 1.21x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.91 sec: 1.22x slower                                                     |
| raytrace                   | 160 ms                                                      | 196 ms: 1.23x slower                                                       |
| genshi_xml                 | 35.5 ms                                                     | 44.0 ms: 1.24x slower                                                      |
| richards_super             | 30.9 ms                                                     | 38.4 ms: 1.25x slower                                                      |
| pylint                     | 211 ms                                                      | 266 ms: 1.26x slower                                                       |
| hexiom                     | 3.89 ms                                                     | 4.92 ms: 1.27x slower                                                      |
| richards                   | 27.3 ms                                                     | 35.8 ms: 1.31x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                               |

Benchmark hidden because not significant (3): bench_thread_pool, xml_etree_iterparse, logging_simple
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240907-3.14.0a0-11fa119-JIT/bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.029x faster
# HPT report

- Reliability score: 98.90% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown