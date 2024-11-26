# Results vs. 3.13.0

- fork: mdboom
- ref: remove_redundant_typ
- machine: windows-amd64
- commit hash: b0f5f3a
- commit date: 2024-09-23
- overall geometric mean: 1.018x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 224 ms: 1.01x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.69 sec: 1.08x slower                                                     |
| html5lib       | 38.9 ms                                                     | 40.1 ms: 1.03x slower                                                      |
| tornado_http   | 93.0 ms                                                     | 84.2 ms: 1.10x faster                                                      |
| Geometric mean | (ref)                                                       | 1.00x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 255 ms: 1.13x faster                                                       |
| async_tree_none            | 226 ms                                                      | 209 ms: 1.08x faster                                                       |
| async_tree_memoization     | 276 ms                                                      | 265 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 389 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 397 ms: 1.05x slower                                                       |
| async_generators           | 223 ms                                                      | 241 ms: 1.08x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 560 ms: 1.08x slower                                                       |
| async_tree_io              | 521 ms                                                      | 570 ms: 1.09x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 14.5 ms: 1.14x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 150 ms: 1.02x slower                                                       |
| float          | 49.9 ms                                                     | 55.8 ms: 1.12x slower                                                      |
| nbody          | 68.4 ms                                                     | 81.8 ms: 1.20x slower                                                      |
| Geometric mean | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 14.8 ms: 1.45x faster                                                      |
| regex_effbot   | 1.58 ms                                                     | 1.55 ms: 1.01x faster                                                      |
| regex_dna      | 115 ms                                                      | 117 ms: 1.01x slower                                                       |
| regex_compile  | 80.5 ms                                                     | 91.4 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.6 us: 1.04x faster                                                      |
| xml_etree_iterparse  | 61.8 ms                                                     | 64.6 ms: 1.04x slower                                                      |
| json_dumps           | 5.92 ms                                                     | 6.23 ms: 1.05x slower                                                      |
| xml_etree_generate   | 54.0 ms                                                     | 57.3 ms: 1.06x slower                                                      |
| xml_etree_process    | 37.0 ms                                                     | 40.3 ms: 1.09x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 149 us: 1.11x slower                                                       |
| pickle_pure_python   | 190 us                                                      | 213 us: 1.13x slower                                                       |
| tomli_loads          | 1.39 sec                                                    | 1.60 sec: 1.15x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 25.4 ms                                                     | 21.9 ms: 1.16x faster                                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 35.5 ms                                                     | 37.5 ms: 1.06x slower                                                      |
| mako            | 6.35 ms                                                     | 6.79 ms: 1.07x slower                                                      |
| genshi_text     | 15.6 ms                                                     | 17.5 ms: 1.12x slower                                                      |
| django_template | 22.4 ms                                                     | 25.7 ms: 1.15x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.10x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 519 us: 16.96x faster                                                      |
| regex_v8                   | 21.4 ms                                                     | 14.8 ms: 1.45x faster                                                      |
| create_gc_cycles           | 1.26 ms                                                     | 883 us: 1.43x faster                                                       |
| bench_mp_pool              | 86.4 ms                                                     | 66.3 ms: 1.30x faster                                                      |
| gc_traversal               | 1.97 ms                                                     | 1.53 ms: 1.29x faster                                                      |
| deepcopy                   | 226 us                                                      | 192 us: 1.18x faster                                                       |
| python_startup             | 25.4 ms                                                     | 21.9 ms: 1.16x faster                                                      |
| async_tree_memoization_tg  | 288 ms                                                      | 255 ms: 1.13x faster                                                       |
| deepcopy_memo              | 23.3 us                                                     | 20.9 us: 1.12x faster                                                      |
| tornado_http               | 93.0 ms                                                     | 84.2 ms: 1.10x faster                                                      |
| async_tree_none            | 226 ms                                                      | 209 ms: 1.08x faster                                                       |
| pathlib                    | 80.9 ms                                                     | 75.6 ms: 1.07x faster                                                      |
| deepcopy_reduce            | 2.06 us                                                     | 1.96 us: 1.05x faster                                                      |
| bench_thread_pool          | 847 us                                                      | 807 us: 1.05x faster                                                       |
| async_tree_memoization     | 276 ms                                                      | 265 ms: 1.04x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.6 us: 1.04x faster                                                      |
| regex_effbot               | 1.58 ms                                                     | 1.55 ms: 1.01x faster                                                      |
| regex_dna                  | 115 ms                                                      | 117 ms: 1.01x slower                                                       |
| 2to3                       | 221 ms                                                      | 224 ms: 1.01x slower                                                       |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 389 ms: 1.02x slower                                                       |
| coverage                   | 45.6 ms                                                     | 46.3 ms: 1.02x slower                                                      |
| pidigits                   | 148 ms                                                      | 150 ms: 1.02x slower                                                       |
| mdp                        | 1.39 sec                                                    | 1.43 sec: 1.03x slower                                                     |
| html5lib                   | 38.9 ms                                                     | 40.1 ms: 1.03x slower                                                      |
| sympy_sum                  | 86.9 ms                                                     | 89.9 ms: 1.03x slower                                                      |
| dulwich_log                | 40.8 ms                                                     | 42.4 ms: 1.04x slower                                                      |
| xml_etree_iterparse        | 61.8 ms                                                     | 64.6 ms: 1.04x slower                                                      |
| typing_runtime_protocols   | 105 us                                                      | 110 us: 1.05x slower                                                       |
| sympy_expand               | 291 ms                                                      | 306 ms: 1.05x slower                                                       |
| sympy_integrate            | 12.5 ms                                                     | 13.1 ms: 1.05x slower                                                      |
| sympy_str                  | 169 ms                                                      | 177 ms: 1.05x slower                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 397 ms: 1.05x slower                                                       |
| json_dumps                 | 5.92 ms                                                     | 6.23 ms: 1.05x slower                                                      |
| telco                      | 4.79 ms                                                     | 5.05 ms: 1.06x slower                                                      |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.60 ms: 1.06x slower                                                      |
| genshi_xml                 | 35.5 ms                                                     | 37.5 ms: 1.06x slower                                                      |
| meteor_contest             | 73.5 ms                                                     | 77.8 ms: 1.06x slower                                                      |
| crypto_pyaes               | 45.4 ms                                                     | 48.1 ms: 1.06x slower                                                      |
| xml_etree_generate         | 54.0 ms                                                     | 57.3 ms: 1.06x slower                                                      |
| mako                       | 6.35 ms                                                     | 6.79 ms: 1.07x slower                                                      |
| pycparser                  | 683 ms                                                      | 734 ms: 1.08x slower                                                       |
| docutils                   | 1.57 sec                                                    | 1.69 sec: 1.08x slower                                                     |
| async_generators           | 223 ms                                                      | 241 ms: 1.08x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 560 ms: 1.08x slower                                                       |
| logging_simple             | 5.96 us                                                     | 6.46 us: 1.08x slower                                                      |
| xml_etree_process          | 37.0 ms                                                     | 40.3 ms: 1.09x slower                                                      |
| generators                 | 19.5 ms                                                     | 21.2 ms: 1.09x slower                                                      |
| async_tree_io              | 521 ms                                                      | 570 ms: 1.09x slower                                                       |
| sqlglot_normalize          | 175 ms                                                      | 191 ms: 1.09x slower                                                       |
| spectral_norm              | 62.8 ms                                                     | 69.0 ms: 1.10x slower                                                      |
| pprint_safe_repr           | 494 ms                                                      | 543 ms: 1.10x slower                                                       |
| sqlglot_optimize           | 32.9 ms                                                     | 36.3 ms: 1.10x slower                                                      |
| logging_format             | 6.26 us                                                     | 6.91 us: 1.10x slower                                                      |
| chaos                      | 38.5 ms                                                     | 42.6 ms: 1.11x slower                                                      |
| pprint_pformat             | 999 ms                                                      | 1.10 sec: 1.11x slower                                                     |
| unpickle_pure_python       | 133 us                                                      | 149 us: 1.11x slower                                                       |
| float                      | 49.9 ms                                                     | 55.8 ms: 1.12x slower                                                      |
| genshi_text                | 15.6 ms                                                     | 17.5 ms: 1.12x slower                                                      |
| nqueens                    | 56.7 ms                                                     | 63.8 ms: 1.13x slower                                                      |
| pickle_pure_python         | 190 us                                                      | 213 us: 1.13x slower                                                       |
| regex_compile              | 80.5 ms                                                     | 91.4 ms: 1.14x slower                                                      |
| pyflate                    | 283 ms                                                      | 322 ms: 1.14x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 14.5 ms: 1.14x slower                                                      |
| hexiom                     | 3.89 ms                                                     | 4.42 ms: 1.14x slower                                                      |
| django_template            | 22.4 ms                                                     | 25.7 ms: 1.15x slower                                                      |
| tomli_loads                | 1.39 sec                                                    | 1.60 sec: 1.15x slower                                                     |
| logging_silent             | 54.6 ns                                                     | 63.0 ns: 1.15x slower                                                      |
| richards_super             | 30.9 ms                                                     | 35.6 ms: 1.15x slower                                                      |
| fannkuch                   | 253 ms                                                      | 293 ms: 1.16x slower                                                       |
| scimark_lu                 | 53.0 ms                                                     | 61.3 ms: 1.16x slower                                                      |
| sqlglot_transpile          | 956 us                                                      | 1.11 ms: 1.16x slower                                                      |
| sqlglot_parse              | 771 us                                                      | 895 us: 1.16x slower                                                       |
| comprehensions             | 10.3 us                                                     | 12.0 us: 1.17x slower                                                      |
| richards                   | 27.3 ms                                                     | 32.0 ms: 1.17x slower                                                      |
| scimark_fft                | 172 ms                                                      | 203 ms: 1.18x slower                                                       |
| deltablue                  | 1.92 ms                                                     | 2.27 ms: 1.18x slower                                                      |
| nbody                      | 68.4 ms                                                     | 81.8 ms: 1.20x slower                                                      |
| scimark_monte_carlo        | 40.8 ms                                                     | 49.0 ms: 1.20x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 92.2 ms: 1.21x slower                                                      |
| raytrace                   | 160 ms                                                      | 194 ms: 1.21x slower                                                       |
| json                       | 3.19 ms                                                     | 4.39 ms: 1.38x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (5): async_tree_none_tg, python_startup_no_site, go, xml_etree_parse, pylint
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240923-3.14.0a0-b0f5f3a/bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.018x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown