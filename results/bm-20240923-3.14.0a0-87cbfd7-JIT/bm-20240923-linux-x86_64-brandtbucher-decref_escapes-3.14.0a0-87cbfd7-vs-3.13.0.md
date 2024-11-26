# Results vs. 3.13.0

- fork: brandtbucher
- ref: decref_escapes
- machine: linux-x86_64
- commit hash: 87cbfd7
- commit date: 2024-09-23
- overall geometric mean: 1.027x faster
- HPT reliability: 94.82%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 278 ms: 1.04x slower                                                  |
| docutils       | 2.59 sec                                               | 2.96 sec: 1.14x slower                                                |
| html5lib       | 64.2 ms                                                | 62.7 ms: 1.02x faster                                                 |
| tornado_http   | 92.4 ms                                                | 94.9 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 388 ms: 1.20x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 395 ms: 1.12x faster                                                  |
| async_tree_none            | 351 ms                                                 | 317 ms: 1.11x faster                                                  |
| async_tree_none_tg         | 321 ms                                                 | 308 ms: 1.04x faster                                                  |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                  |
| async_tree_io_tg           | 857 ms                                                 | 874 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 557 ms: 1.02x slower                                                  |
| async_tree_io              | 842 ms                                                 | 862 ms: 1.02x slower                                                  |
| async_generators           | 436 ms                                                 | 457 ms: 1.05x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 70.6 ms: 1.12x faster                                                 |
| nbody          | 87.0 ms                                                | 81.4 ms: 1.07x faster                                                 |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.1 ms: 1.09x faster                                                 |
| regex_effbot   | 3.73 ms                                                | 3.61 ms: 1.03x faster                                                 |
| regex_dna      | 218 ms                                                 | 215 ms: 1.02x faster                                                  |
| regex_compile  | 132 ms                                                 | 142 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|---------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_generate  | 86.7 ms                                                | 78.2 ms: 1.11x faster                                                 |
| xml_etree_process   | 60.6 ms                                                | 55.0 ms: 1.10x faster                                                 |
| tomli_loads         | 2.14 sec                                               | 1.95 sec: 1.10x faster                                                |
| xml_etree_parse     | 156 ms                                                 | 146 ms: 1.07x faster                                                  |
| json_dumps          | 10.6 ms                                                | 10.1 ms: 1.05x faster                                                 |
| xml_etree_iterparse | 101 ms                                                 | 99.3 ms: 1.02x faster                                                 |
| json_loads          | 27.2 us                                                | 26.7 us: 1.02x faster                                                 |
| pickle_pure_python  | 310 us                                                 | 308 us: 1.01x faster                                                  |
| Geometric mean      | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.18x faster                                                 |
| python_startup_no_site | 6.96 ms                                                | 7.06 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.77 ms: 1.13x faster                                                 |
| django_template | 35.2 ms                                                | 36.4 ms: 1.04x slower                                                 |
| genshi_text     | 23.5 ms                                                | 24.9 ms: 1.06x slower                                                 |
| genshi_xml      | 50.9 ms                                                | 60.0 ms: 1.18x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 27.0 us: 1.45x faster                                                 |
| deepcopy                   | 358 us                                                 | 260 us: 1.38x faster                                                  |
| create_gc_cycles           | 2.41 ms                                                | 1.76 ms: 1.37x faster                                                 |
| deepcopy_reduce            | 3.20 us                                                | 2.62 us: 1.22x faster                                                 |
| async_tree_memoization_tg  | 464 ms                                                 | 388 ms: 1.20x faster                                                  |
| python_startup             | 12.5 ms                                                | 10.5 ms: 1.18x faster                                                 |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.32 ms: 1.17x faster                                                 |
| richards_super             | 54.9 ms                                                | 47.2 ms: 1.16x faster                                                 |
| scimark_fft                | 364 ms                                                 | 315 ms: 1.16x faster                                                  |
| richards                   | 48.7 ms                                                | 42.7 ms: 1.14x faster                                                 |
| mako                       | 11.1 ms                                                | 9.77 ms: 1.13x faster                                                 |
| float                      | 79.2 ms                                                | 70.6 ms: 1.12x faster                                                 |
| async_tree_memoization     | 442 ms                                                 | 395 ms: 1.12x faster                                                  |
| gc_traversal               | 4.37 ms                                                | 3.91 ms: 1.12x faster                                                 |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.12x faster                                                  |
| crypto_pyaes               | 75.3 ms                                                | 67.6 ms: 1.11x faster                                                 |
| xml_etree_generate         | 86.7 ms                                                | 78.2 ms: 1.11x faster                                                 |
| async_tree_none            | 351 ms                                                 | 317 ms: 1.11x faster                                                  |
| xml_etree_process          | 60.6 ms                                                | 55.0 ms: 1.10x faster                                                 |
| tomli_loads                | 2.14 sec                                               | 1.95 sec: 1.10x faster                                                |
| pathlib                    | 17.5 ms                                                | 16.1 ms: 1.09x faster                                                 |
| regex_v8                   | 26.2 ms                                                | 24.1 ms: 1.09x faster                                                 |
| go                         | 144 ms                                                 | 133 ms: 1.08x faster                                                  |
| mdp                        | 2.72 sec                                               | 2.52 sec: 1.08x faster                                                |
| scimark_monte_carlo        | 67.4 ms                                                | 63.1 ms: 1.07x faster                                                 |
| nbody                      | 87.0 ms                                                | 81.4 ms: 1.07x faster                                                 |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.07x faster                                                  |
| fannkuch                   | 404 ms                                                 | 380 ms: 1.06x faster                                                  |
| json                       | 5.36 ms                                                | 5.04 ms: 1.06x faster                                                 |
| pyflate                    | 471 ms                                                 | 443 ms: 1.06x faster                                                  |
| bpe_tokeniser              | 4.75 sec                                               | 4.47 sec: 1.06x faster                                                |
| telco                      | 8.54 ms                                                | 8.06 ms: 1.06x faster                                                 |
| json_dumps                 | 10.6 ms                                                | 10.1 ms: 1.05x faster                                                 |
| async_tree_none_tg         | 321 ms                                                 | 308 ms: 1.04x faster                                                  |
| scimark_sor                | 124 ms                                                 | 119 ms: 1.04x faster                                                  |
| regex_effbot               | 3.73 ms                                                | 3.61 ms: 1.03x faster                                                 |
| thrift                     | 809 us                                                 | 786 us: 1.03x faster                                                  |
| meteor_contest             | 109 ms                                                 | 106 ms: 1.03x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.03x faster                                                |
| html5lib                   | 64.2 ms                                                | 62.7 ms: 1.02x faster                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 99.3 ms: 1.02x faster                                                 |
| json_loads                 | 27.2 us                                                | 26.7 us: 1.02x faster                                                 |
| logging_format             | 6.40 us                                                | 6.28 us: 1.02x faster                                                 |
| typing_runtime_protocols   | 165 us                                                 | 162 us: 1.02x faster                                                  |
| regex_dna                  | 218 ms                                                 | 215 ms: 1.02x faster                                                  |
| pickle_pure_python         | 310 us                                                 | 308 us: 1.01x faster                                                  |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                  |
| coverage                   | 84.0 ms                                                | 84.4 ms: 1.01x slower                                                 |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                  |
| deltablue                  | 3.23 ms                                                | 3.27 ms: 1.01x slower                                                 |
| python_startup_no_site     | 6.96 ms                                                | 7.06 ms: 1.01x slower                                                 |
| logging_silent             | 102 ns                                                 | 103 ns: 1.02x slower                                                  |
| comprehensions             | 16.5 us                                                | 16.8 us: 1.02x slower                                                 |
| async_tree_io_tg           | 857 ms                                                 | 874 ms: 1.02x slower                                                  |
| bench_thread_pool          | 822 us                                                 | 839 us: 1.02x slower                                                  |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 557 ms: 1.02x slower                                                  |
| chaos                      | 58.1 ms                                                | 59.4 ms: 1.02x slower                                                 |
| async_tree_io              | 842 ms                                                 | 862 ms: 1.02x slower                                                  |
| pprint_pformat             | 1.49 sec                                               | 1.53 sec: 1.02x slower                                                |
| tornado_http               | 92.4 ms                                                | 94.9 ms: 1.03x slower                                                 |
| django_template            | 35.2 ms                                                | 36.4 ms: 1.04x slower                                                 |
| 2to3                       | 267 ms                                                 | 278 ms: 1.04x slower                                                  |
| raytrace                   | 267 ms                                                 | 279 ms: 1.04x slower                                                  |
| async_generators           | 436 ms                                                 | 457 ms: 1.05x slower                                                  |
| sqlglot_normalize          | 108 ms                                                 | 114 ms: 1.06x slower                                                  |
| genshi_text                | 23.5 ms                                                | 24.9 ms: 1.06x slower                                                 |
| sqlglot_parse              | 1.27 ms                                                | 1.35 ms: 1.06x slower                                                 |
| dulwich_log                | 64.3 ms                                                | 68.5 ms: 1.06x slower                                                 |
| regex_compile              | 132 ms                                                 | 142 ms: 1.08x slower                                                  |
| sqlglot_transpile          | 1.58 ms                                                | 1.71 ms: 1.08x slower                                                 |
| sqlglot_optimize           | 53.7 ms                                                | 58.2 ms: 1.08x slower                                                 |
| sympy_str                  | 275 ms                                                 | 299 ms: 1.09x slower                                                  |
| sympy_expand               | 463 ms                                                 | 505 ms: 1.09x slower                                                  |
| nqueens                    | 78.4 ms                                                | 86.1 ms: 1.10x slower                                                 |
| hexiom                     | 6.16 ms                                                | 7.00 ms: 1.14x slower                                                 |
| generators                 | 29.0 ms                                                | 33.0 ms: 1.14x slower                                                 |
| sympy_sum                  | 150 ms                                                 | 172 ms: 1.14x slower                                                  |
| docutils                   | 2.59 sec                                               | 2.96 sec: 1.14x slower                                                |
| sympy_integrate            | 19.9 ms                                                | 22.7 ms: 1.14x slower                                                 |
| genshi_xml                 | 50.9 ms                                                | 60.0 ms: 1.18x slower                                                 |
| pylint                     | 313 ms                                                 | 374 ms: 1.20x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (7): logging_simple, async_tree_cpu_io_mixed, scimark_lu, pprint_safe_repr, coroutines, bench_mp_pool, unpickle_pure_python
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240923-3.14.0a0-87cbfd7-JIT/bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.027x faster
# HPT report

- Reliability score: 94.82% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x