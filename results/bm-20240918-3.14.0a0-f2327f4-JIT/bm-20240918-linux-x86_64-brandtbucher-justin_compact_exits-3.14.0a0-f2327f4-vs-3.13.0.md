# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_compact_exits
- machine: linux-x86_64
- commit hash: f2327f4
- commit date: 2024-09-18
- overall geometric mean: 1.014x faster
- HPT reliability: 64.10%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 282 ms: 1.06x slower                                                        |
| docutils       | 2.59 sec                                               | 3.20 sec: 1.23x slower                                                      |
| html5lib       | 64.2 ms                                                | 66.5 ms: 1.04x slower                                                       |
| tornado_http   | 92.4 ms                                                | 95.0 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                  | 1.09x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 552 ms                                                 | 556 ms: 1.01x slower                                                        |
| coroutines                 | 22.7 ms                                                | 23.2 ms: 1.02x slower                                                       |
| async_tree_none            | 351 ms                                                 | 360 ms: 1.03x slower                                                        |
| async_tree_memoization     | 442 ms                                                 | 455 ms: 1.03x slower                                                        |
| async_generators           | 436 ms                                                 | 457 ms: 1.05x slower                                                        |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 605 ms: 1.05x slower                                                        |
| async_tree_memoization_tg  | 464 ms                                                 | 513 ms: 1.11x slower                                                        |
| async_tree_io              | 842 ms                                                 | 941 ms: 1.12x slower                                                        |
| async_tree_io_tg           | 857 ms                                                 | 1.02 sec: 1.19x slower                                                      |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 666 ms: 1.22x slower                                                        |
| async_tree_none_tg         | 321 ms                                                 | 401 ms: 1.25x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.09x slower                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 72.1 ms: 1.10x faster                                                       |
| nbody          | 87.0 ms                                                | 81.1 ms: 1.07x faster                                                       |
| pidigits       | 186 ms                                                 | 185 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.2 ms: 1.04x faster                                                       |
| regex_effbot   | 3.73 ms                                                | 3.65 ms: 1.02x faster                                                       |
| regex_dna      | 218 ms                                                 | 221 ms: 1.01x slower                                                        |
| regex_compile  | 132 ms                                                 | 138 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 86.7 ms                                                | 77.4 ms: 1.12x faster                                                       |
| xml_etree_process    | 60.6 ms                                                | 54.2 ms: 1.12x faster                                                       |
| tomli_loads          | 2.14 sec                                               | 1.92 sec: 1.11x faster                                                      |
| json_dumps           | 10.6 ms                                                | 10.2 ms: 1.04x faster                                                       |
| xml_etree_parse      | 156 ms                                                 | 150 ms: 1.04x faster                                                        |
| pickle_pure_python   | 310 us                                                 | 305 us: 1.02x faster                                                        |
| json_loads           | 27.2 us                                                | 27.0 us: 1.01x faster                                                       |
| unpickle_pure_python | 216 us                                                 | 214 us: 1.01x faster                                                        |
| xml_etree_iterparse  | 101 ms                                                 | 104 ms: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.6 ms: 1.18x faster                                                       |
| python_startup_no_site | 6.96 ms                                                | 7.09 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.0 ms: 1.11x faster                                                       |
| django_template | 35.2 ms                                                | 35.7 ms: 1.02x slower                                                       |
| genshi_text     | 23.5 ms                                                | 26.0 ms: 1.10x slower                                                       |
| genshi_xml      | 50.9 ms                                                | 58.8 ms: 1.15x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 26.9 us: 1.45x faster                                                       |
| deepcopy                   | 358 us                                                 | 250 us: 1.43x faster                                                        |
| create_gc_cycles           | 2.41 ms                                                | 1.77 ms: 1.36x faster                                                       |
| richards                   | 48.7 ms                                                | 39.5 ms: 1.23x faster                                                       |
| deepcopy_reduce            | 3.20 us                                                | 2.65 us: 1.21x faster                                                       |
| richards_super             | 54.9 ms                                                | 45.6 ms: 1.20x faster                                                       |
| scimark_fft                | 364 ms                                                 | 308 ms: 1.18x faster                                                        |
| python_startup             | 12.5 ms                                                | 10.6 ms: 1.18x faster                                                       |
| spectral_norm              | 115 ms                                                 | 98.6 ms: 1.17x faster                                                       |
| go                         | 144 ms                                                 | 126 ms: 1.14x faster                                                        |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.42 ms: 1.14x faster                                                       |
| crypto_pyaes               | 75.3 ms                                                | 66.5 ms: 1.13x faster                                                       |
| xml_etree_generate         | 86.7 ms                                                | 77.4 ms: 1.12x faster                                                       |
| xml_etree_process          | 60.6 ms                                                | 54.2 ms: 1.12x faster                                                       |
| tomli_loads                | 2.14 sec                                               | 1.92 sec: 1.11x faster                                                      |
| pathlib                    | 17.5 ms                                                | 15.8 ms: 1.11x faster                                                       |
| mako                       | 11.1 ms                                                | 10.0 ms: 1.11x faster                                                       |
| float                      | 79.2 ms                                                | 72.1 ms: 1.10x faster                                                       |
| gc_traversal               | 4.37 ms                                                | 4.04 ms: 1.08x faster                                                       |
| mdp                        | 2.72 sec                                               | 2.52 sec: 1.08x faster                                                      |
| scimark_monte_carlo        | 67.4 ms                                                | 62.6 ms: 1.08x faster                                                       |
| json                       | 5.36 ms                                                | 4.99 ms: 1.07x faster                                                       |
| fannkuch                   | 404 ms                                                 | 377 ms: 1.07x faster                                                        |
| nbody                      | 87.0 ms                                                | 81.1 ms: 1.07x faster                                                       |
| telco                      | 8.54 ms                                                | 8.07 ms: 1.06x faster                                                       |
| scimark_sor                | 124 ms                                                 | 117 ms: 1.05x faster                                                        |
| pyflate                    | 471 ms                                                 | 452 ms: 1.04x faster                                                        |
| regex_v8                   | 26.2 ms                                                | 25.2 ms: 1.04x faster                                                       |
| json_dumps                 | 10.6 ms                                                | 10.2 ms: 1.04x faster                                                       |
| xml_etree_parse            | 156 ms                                                 | 150 ms: 1.04x faster                                                        |
| logging_format             | 6.40 us                                                | 6.20 us: 1.03x faster                                                       |
| thrift                     | 809 us                                                 | 791 us: 1.02x faster                                                        |
| regex_effbot               | 3.73 ms                                                | 3.65 ms: 1.02x faster                                                       |
| pprint_pformat             | 1.49 sec                                               | 1.46 sec: 1.02x faster                                                      |
| pickle_pure_python         | 310 us                                                 | 305 us: 1.02x faster                                                        |
| scimark_lu                 | 113 ms                                                 | 111 ms: 1.02x faster                                                        |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.02x faster                                                        |
| logging_simple             | 5.72 us                                                | 5.64 us: 1.01x faster                                                       |
| json_loads                 | 27.2 us                                                | 27.0 us: 1.01x faster                                                       |
| bpe_tokeniser              | 4.75 sec                                               | 4.71 sec: 1.01x faster                                                      |
| unpickle_pure_python       | 216 us                                                 | 214 us: 1.01x faster                                                        |
| pidigits                   | 186 ms                                                 | 185 ms: 1.01x faster                                                        |
| deltablue                  | 3.23 ms                                                | 3.21 ms: 1.00x faster                                                       |
| asyncio_websockets         | 552 ms                                                 | 556 ms: 1.01x slower                                                        |
| regex_dna                  | 218 ms                                                 | 221 ms: 1.01x slower                                                        |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.01x slower                                                       |
| chaos                      | 58.1 ms                                                | 58.9 ms: 1.02x slower                                                       |
| django_template            | 35.2 ms                                                | 35.7 ms: 1.02x slower                                                       |
| python_startup_no_site     | 6.96 ms                                                | 7.09 ms: 1.02x slower                                                       |
| bench_thread_pool          | 822 us                                                 | 837 us: 1.02x slower                                                        |
| coroutines                 | 22.7 ms                                                | 23.2 ms: 1.02x slower                                                       |
| coverage                   | 84.0 ms                                                | 85.9 ms: 1.02x slower                                                       |
| xml_etree_iterparse        | 101 ms                                                 | 104 ms: 1.03x slower                                                        |
| async_tree_none            | 351 ms                                                 | 360 ms: 1.03x slower                                                        |
| tornado_http               | 92.4 ms                                                | 95.0 ms: 1.03x slower                                                       |
| async_tree_memoization     | 442 ms                                                 | 455 ms: 1.03x slower                                                        |
| sqlglot_normalize          | 108 ms                                                 | 111 ms: 1.03x slower                                                        |
| html5lib                   | 64.2 ms                                                | 66.5 ms: 1.04x slower                                                       |
| logging_silent             | 102 ns                                                 | 105 ns: 1.04x slower                                                        |
| raytrace                   | 267 ms                                                 | 277 ms: 1.04x slower                                                        |
| regex_compile              | 132 ms                                                 | 138 ms: 1.04x slower                                                        |
| async_generators           | 436 ms                                                 | 457 ms: 1.05x slower                                                        |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 605 ms: 1.05x slower                                                        |
| dulwich_log                | 64.3 ms                                                | 67.6 ms: 1.05x slower                                                       |
| sqlglot_parse              | 1.27 ms                                                | 1.35 ms: 1.06x slower                                                       |
| 2to3                       | 267 ms                                                 | 282 ms: 1.06x slower                                                        |
| sqlglot_optimize           | 53.7 ms                                                | 57.1 ms: 1.06x slower                                                       |
| sympy_str                  | 275 ms                                                 | 296 ms: 1.08x slower                                                        |
| nqueens                    | 78.4 ms                                                | 84.6 ms: 1.08x slower                                                       |
| sympy_expand               | 463 ms                                                 | 503 ms: 1.08x slower                                                        |
| sqlglot_transpile          | 1.58 ms                                                | 1.73 ms: 1.09x slower                                                       |
| genshi_text                | 23.5 ms                                                | 26.0 ms: 1.10x slower                                                       |
| async_tree_memoization_tg  | 464 ms                                                 | 513 ms: 1.11x slower                                                        |
| hexiom                     | 6.16 ms                                                | 6.83 ms: 1.11x slower                                                       |
| async_tree_io              | 842 ms                                                 | 941 ms: 1.12x slower                                                        |
| generators                 | 29.0 ms                                                | 32.6 ms: 1.13x slower                                                       |
| sympy_sum                  | 150 ms                                                 | 171 ms: 1.14x slower                                                        |
| sympy_integrate            | 19.9 ms                                                | 22.7 ms: 1.14x slower                                                       |
| genshi_xml                 | 50.9 ms                                                | 58.8 ms: 1.15x slower                                                       |
| async_tree_io_tg           | 857 ms                                                 | 1.02 sec: 1.19x slower                                                      |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 666 ms: 1.22x slower                                                        |
| docutils                   | 2.59 sec                                               | 3.20 sec: 1.23x slower                                                      |
| async_tree_none_tg         | 321 ms                                                 | 401 ms: 1.25x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (5): pprint_safe_repr, typing_runtime_protocols, bench_mp_pool, pylint, pycparser
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240918-3.14.0a0-f2327f4-JIT/bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.014x faster
# HPT report

- Reliability score: 64.10% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.98x