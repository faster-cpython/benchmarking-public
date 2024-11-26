# Results vs. 3.13.0

- fork: brandtbucher
- ref: tier_two_constants
- machine: linux-x86_64
- commit hash: eb54546
- commit date: 2024-09-12
- overall geometric mean: 1.033x faster
- HPT reliability: 89.33%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 276 ms: 1.03x slower                                                      |
| docutils       | 2.59 sec                                               | 2.95 sec: 1.14x slower                                                    |
| html5lib       | 64.2 ms                                                | 64.5 ms: 1.00x slower                                                     |
| tornado_http   | 92.4 ms                                                | 94.4 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                  | 1.05x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 387 ms: 1.20x faster                                                      |
| async_tree_memoization     | 442 ms                                                 | 394 ms: 1.12x faster                                                      |
| async_tree_none            | 351 ms                                                 | 316 ms: 1.11x faster                                                      |
| async_tree_none_tg         | 321 ms                                                 | 307 ms: 1.04x faster                                                      |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 569 ms: 1.01x faster                                                      |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                      |
| coroutines                 | 22.7 ms                                                | 22.8 ms: 1.01x slower                                                     |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 555 ms: 1.02x slower                                                      |
| async_tree_io_tg           | 857 ms                                                 | 875 ms: 1.02x slower                                                      |
| async_generators           | 436 ms                                                 | 456 ms: 1.05x slower                                                      |
| async_tree_io              | 842 ms                                                 | 887 ms: 1.05x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 69.9 ms: 1.13x faster                                                     |
| nbody          | 87.0 ms                                                | 80.9 ms: 1.07x faster                                                     |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.07x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.1 ms: 1.09x faster                                                     |
| regex_dna      | 218 ms                                                 | 224 ms: 1.02x slower                                                      |
| regex_effbot   | 3.73 ms                                                | 3.86 ms: 1.03x slower                                                     |
| regex_compile  | 132 ms                                                 | 140 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|---------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_generate  | 86.7 ms                                                | 77.0 ms: 1.13x faster                                                     |
| tomli_loads         | 2.14 sec                                               | 1.91 sec: 1.12x faster                                                    |
| xml_etree_process   | 60.6 ms                                                | 54.4 ms: 1.12x faster                                                     |
| xml_etree_parse     | 156 ms                                                 | 146 ms: 1.07x faster                                                      |
| json_dumps          | 10.6 ms                                                | 9.96 ms: 1.06x faster                                                     |
| xml_etree_iterparse | 101 ms                                                 | 99.1 ms: 1.02x faster                                                     |
| pickle_pure_python  | 310 us                                                 | 306 us: 1.01x faster                                                      |
| json_loads          | 27.2 us                                                | 27.1 us: 1.01x faster                                                     |
| Geometric mean      | (ref)                                                  | 1.06x faster                                                              |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.6 ms: 1.18x faster                                                     |
| python_startup_no_site | 6.96 ms                                                | 7.07 ms: 1.02x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.78 ms: 1.13x faster                                                     |
| django_template | 35.2 ms                                                | 36.0 ms: 1.02x slower                                                     |
| genshi_text     | 23.5 ms                                                | 24.3 ms: 1.03x slower                                                     |
| genshi_xml      | 50.9 ms                                                | 56.8 ms: 1.12x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 26.9 us: 1.45x faster                                                     |
| deepcopy                   | 358 us                                                 | 259 us: 1.38x faster                                                      |
| create_gc_cycles           | 2.41 ms                                                | 1.76 ms: 1.37x faster                                                     |
| richards                   | 48.7 ms                                                | 39.7 ms: 1.23x faster                                                     |
| richards_super             | 54.9 ms                                                | 45.1 ms: 1.22x faster                                                     |
| async_tree_memoization_tg  | 464 ms                                                 | 387 ms: 1.20x faster                                                      |
| deepcopy_reduce            | 3.20 us                                                | 2.69 us: 1.19x faster                                                     |
| spectral_norm              | 115 ms                                                 | 97.4 ms: 1.18x faster                                                     |
| python_startup             | 12.5 ms                                                | 10.6 ms: 1.18x faster                                                     |
| scimark_fft                | 364 ms                                                 | 311 ms: 1.17x faster                                                      |
| gc_traversal               | 4.37 ms                                                | 3.79 ms: 1.15x faster                                                     |
| crypto_pyaes               | 75.3 ms                                                | 66.2 ms: 1.14x faster                                                     |
| float                      | 79.2 ms                                                | 69.9 ms: 1.13x faster                                                     |
| mako                       | 11.1 ms                                                | 9.78 ms: 1.13x faster                                                     |
| xml_etree_generate         | 86.7 ms                                                | 77.0 ms: 1.13x faster                                                     |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.49 ms: 1.12x faster                                                     |
| tomli_loads                | 2.14 sec                                               | 1.91 sec: 1.12x faster                                                    |
| async_tree_memoization     | 442 ms                                                 | 394 ms: 1.12x faster                                                      |
| xml_etree_process          | 60.6 ms                                                | 54.4 ms: 1.12x faster                                                     |
| async_tree_none            | 351 ms                                                 | 316 ms: 1.11x faster                                                      |
| pathlib                    | 17.5 ms                                                | 15.8 ms: 1.11x faster                                                     |
| go                         | 144 ms                                                 | 132 ms: 1.09x faster                                                      |
| regex_v8                   | 26.2 ms                                                | 24.1 ms: 1.09x faster                                                     |
| fannkuch                   | 404 ms                                                 | 373 ms: 1.08x faster                                                      |
| bpe_tokeniser              | 4.75 sec                                               | 4.41 sec: 1.08x faster                                                    |
| nbody                      | 87.0 ms                                                | 80.9 ms: 1.07x faster                                                     |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.07x faster                                                      |
| scimark_sor                | 124 ms                                                 | 116 ms: 1.07x faster                                                      |
| scimark_monte_carlo        | 67.4 ms                                                | 63.2 ms: 1.07x faster                                                     |
| json_dumps                 | 10.6 ms                                                | 9.96 ms: 1.06x faster                                                     |
| telco                      | 8.54 ms                                                | 8.06 ms: 1.06x faster                                                     |
| mdp                        | 2.72 sec                                               | 2.58 sec: 1.06x faster                                                    |
| pyflate                    | 471 ms                                                 | 449 ms: 1.05x faster                                                      |
| logging_format             | 6.40 us                                                | 6.12 us: 1.05x faster                                                     |
| json                       | 5.36 ms                                                | 5.13 ms: 1.05x faster                                                     |
| async_tree_none_tg         | 321 ms                                                 | 307 ms: 1.04x faster                                                      |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.04x faster                                                    |
| thrift                     | 809 us                                                 | 784 us: 1.03x faster                                                      |
| xml_etree_iterparse        | 101 ms                                                 | 99.1 ms: 1.02x faster                                                     |
| logging_simple             | 5.72 us                                                | 5.61 us: 1.02x faster                                                     |
| typing_runtime_protocols   | 165 us                                                 | 161 us: 1.02x faster                                                      |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.02x faster                                                      |
| pickle_pure_python         | 310 us                                                 | 306 us: 1.01x faster                                                      |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 569 ms: 1.01x faster                                                      |
| deltablue                  | 3.23 ms                                                | 3.20 ms: 1.01x faster                                                     |
| json_loads                 | 27.2 us                                                | 27.1 us: 1.01x faster                                                     |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                      |
| coverage                   | 84.0 ms                                                | 84.4 ms: 1.00x slower                                                     |
| html5lib                   | 64.2 ms                                                | 64.5 ms: 1.00x slower                                                     |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                      |
| coroutines                 | 22.7 ms                                                | 22.8 ms: 1.01x slower                                                     |
| logging_silent             | 102 ns                                                 | 103 ns: 1.01x slower                                                      |
| chaos                      | 58.1 ms                                                | 58.8 ms: 1.01x slower                                                     |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.01x slower                                                     |
| python_startup_no_site     | 6.96 ms                                                | 7.07 ms: 1.02x slower                                                     |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 555 ms: 1.02x slower                                                      |
| bench_thread_pool          | 822 us                                                 | 837 us: 1.02x slower                                                      |
| tornado_http               | 92.4 ms                                                | 94.4 ms: 1.02x slower                                                     |
| async_tree_io_tg           | 857 ms                                                 | 875 ms: 1.02x slower                                                      |
| regex_dna                  | 218 ms                                                 | 224 ms: 1.02x slower                                                      |
| django_template            | 35.2 ms                                                | 36.0 ms: 1.02x slower                                                     |
| genshi_text                | 23.5 ms                                                | 24.3 ms: 1.03x slower                                                     |
| 2to3                       | 267 ms                                                 | 276 ms: 1.03x slower                                                      |
| regex_effbot               | 3.73 ms                                                | 3.86 ms: 1.03x slower                                                     |
| sqlglot_normalize          | 108 ms                                                 | 112 ms: 1.04x slower                                                      |
| pprint_pformat             | 1.49 sec                                               | 1.55 sec: 1.04x slower                                                    |
| raytrace                   | 267 ms                                                 | 277 ms: 1.04x slower                                                      |
| pprint_safe_repr           | 728 ms                                                 | 757 ms: 1.04x slower                                                      |
| async_generators           | 436 ms                                                 | 456 ms: 1.05x slower                                                      |
| sqlglot_parse              | 1.27 ms                                                | 1.33 ms: 1.05x slower                                                     |
| sqlglot_transpile          | 1.58 ms                                                | 1.67 ms: 1.05x slower                                                     |
| async_tree_io              | 842 ms                                                 | 887 ms: 1.05x slower                                                      |
| regex_compile              | 132 ms                                                 | 140 ms: 1.06x slower                                                      |
| dulwich_log                | 64.3 ms                                                | 68.3 ms: 1.06x slower                                                     |
| sqlglot_optimize           | 53.7 ms                                                | 57.8 ms: 1.08x slower                                                     |
| sympy_str                  | 275 ms                                                 | 296 ms: 1.08x slower                                                      |
| sympy_expand               | 463 ms                                                 | 500 ms: 1.08x slower                                                      |
| nqueens                    | 78.4 ms                                                | 85.1 ms: 1.09x slower                                                     |
| hexiom                     | 6.16 ms                                                | 6.78 ms: 1.10x slower                                                     |
| genshi_xml                 | 50.9 ms                                                | 56.8 ms: 1.12x slower                                                     |
| sympy_integrate            | 19.9 ms                                                | 22.6 ms: 1.13x slower                                                     |
| generators                 | 29.0 ms                                                | 32.9 ms: 1.14x slower                                                     |
| sympy_sum                  | 150 ms                                                 | 171 ms: 1.14x slower                                                      |
| docutils                   | 2.59 sec                                               | 2.95 sec: 1.14x slower                                                    |
| pylint                     | 313 ms                                                 | 372 ms: 1.19x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (3): scimark_lu, bench_mp_pool, unpickle_pure_python
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240912-3.14.0a0-eb54546-JIT/bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.033x faster
# HPT report

- Reliability score: 89.33% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x