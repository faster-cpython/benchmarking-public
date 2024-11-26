# Results vs. 3.13.0

- fork: python
- ref: e913d2c87f1ae4e7a4ae
- machine: linux-x86_64
- commit hash: e913d2c
- commit date: 2024-08-15
- overall geometric mean: 1.037x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 260 ms: 1.02x faster                                                  |
| docutils       | 2.59 sec                                               | 2.70 sec: 1.04x slower                                                |
| html5lib       | 64.2 ms                                                | 64.5 ms: 1.01x slower                                                 |
| tornado_http   | 92.4 ms                                                | 90.2 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 388 ms: 1.20x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 397 ms: 1.11x faster                                                  |
| async_tree_none            | 351 ms                                                 | 322 ms: 1.09x faster                                                  |
| async_tree_none_tg         | 321 ms                                                 | 297 ms: 1.08x faster                                                  |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 556 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 527 ms: 1.04x faster                                                  |
| coroutines                 | 22.7 ms                                                | 22.9 ms: 1.01x slower                                                 |
| asyncio_websockets         | 552 ms                                                 | 558 ms: 1.01x slower                                                  |
| async_tree_io_tg           | 857 ms                                                 | 885 ms: 1.03x slower                                                  |
| async_tree_io              | 842 ms                                                 | 901 ms: 1.07x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (1): async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 87.0 ms                                                | 84.7 ms: 1.03x faster                                                 |
| float          | 79.2 ms                                                | 77.9 ms: 1.02x faster                                                 |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 23.9 ms: 1.10x faster                                                 |
| regex_effbot   | 3.73 ms                                                | 3.62 ms: 1.03x faster                                                 |
| regex_compile  | 132 ms                                                 | 129 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 310 us                                                 | 298 us: 1.04x faster                                                  |
| tomli_loads          | 2.14 sec                                               | 2.06 sec: 1.04x faster                                                |
| unpickle_pure_python | 216 us                                                 | 209 us: 1.03x faster                                                  |
| xml_etree_process    | 60.6 ms                                                | 59.1 ms: 1.03x faster                                                 |
| json_dumps           | 10.6 ms                                                | 10.4 ms: 1.02x faster                                                 |
| xml_etree_generate   | 86.7 ms                                                | 86.3 ms: 1.00x faster                                                 |
| xml_etree_iterparse  | 101 ms                                                 | 104 ms: 1.03x slower                                                  |
| json_loads           | 27.2 us                                                | 28.5 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                 |
| python_startup_no_site | 6.96 ms                                                | 7.06 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 22.5 ms: 1.04x faster                                                 |
| django_template | 35.2 ms                                                | 33.8 ms: 1.04x faster                                                 |
| genshi_xml      | 50.9 ms                                                | 50.0 ms: 1.02x faster                                                 |
| mako            | 11.1 ms                                                | 11.1 ms: 1.00x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 258 us: 1.39x faster                                                  |
| create_gc_cycles           | 2.41 ms                                                | 1.74 ms: 1.39x faster                                                 |
| deepcopy_memo              | 39.1 us                                                | 29.1 us: 1.34x faster                                                 |
| gc_traversal               | 4.37 ms                                                | 3.57 ms: 1.22x faster                                                 |
| async_tree_memoization_tg  | 464 ms                                                 | 388 ms: 1.20x faster                                                  |
| deepcopy_reduce            | 3.20 us                                                | 2.68 us: 1.19x faster                                                 |
| python_startup             | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                 |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.52 ms: 1.12x faster                                                 |
| async_tree_memoization     | 442 ms                                                 | 397 ms: 1.11x faster                                                  |
| regex_v8                   | 26.2 ms                                                | 23.9 ms: 1.10x faster                                                 |
| async_tree_none            | 351 ms                                                 | 322 ms: 1.09x faster                                                  |
| pathlib                    | 17.5 ms                                                | 16.2 ms: 1.08x faster                                                 |
| async_tree_none_tg         | 321 ms                                                 | 297 ms: 1.08x faster                                                  |
| richards                   | 48.7 ms                                                | 45.1 ms: 1.08x faster                                                 |
| richards_super             | 54.9 ms                                                | 51.2 ms: 1.07x faster                                                 |
| logging_format             | 6.40 us                                                | 6.03 us: 1.06x faster                                                 |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.06x faster                                                |
| raytrace                   | 267 ms                                                 | 253 ms: 1.06x faster                                                  |
| logging_silent             | 102 ns                                                 | 96.5 ns: 1.05x faster                                                 |
| logging_simple             | 5.72 us                                                | 5.46 us: 1.05x faster                                                 |
| telco                      | 8.54 ms                                                | 8.15 ms: 1.05x faster                                                 |
| generators                 | 29.0 ms                                                | 27.7 ms: 1.05x faster                                                 |
| genshi_text                | 23.5 ms                                                | 22.5 ms: 1.04x faster                                                 |
| bench_thread_pool          | 822 us                                                 | 787 us: 1.04x faster                                                  |
| go                         | 144 ms                                                 | 138 ms: 1.04x faster                                                  |
| pickle_pure_python         | 310 us                                                 | 298 us: 1.04x faster                                                  |
| django_template            | 35.2 ms                                                | 33.8 ms: 1.04x faster                                                 |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 556 ms: 1.04x faster                                                  |
| tomli_loads                | 2.14 sec                                               | 2.06 sec: 1.04x faster                                                |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 527 ms: 1.04x faster                                                  |
| regex_effbot               | 3.73 ms                                                | 3.62 ms: 1.03x faster                                                 |
| thrift                     | 809 us                                                 | 784 us: 1.03x faster                                                  |
| unpickle_pure_python       | 216 us                                                 | 209 us: 1.03x faster                                                  |
| regex_compile              | 132 ms                                                 | 129 ms: 1.03x faster                                                  |
| nbody                      | 87.0 ms                                                | 84.7 ms: 1.03x faster                                                 |
| xml_etree_process          | 60.6 ms                                                | 59.1 ms: 1.03x faster                                                 |
| tornado_http               | 92.4 ms                                                | 90.2 ms: 1.03x faster                                                 |
| 2to3                       | 267 ms                                                 | 260 ms: 1.02x faster                                                  |
| scimark_fft                | 364 ms                                                 | 356 ms: 1.02x faster                                                  |
| json_dumps                 | 10.6 ms                                                | 10.4 ms: 1.02x faster                                                 |
| genshi_xml                 | 50.9 ms                                                | 50.0 ms: 1.02x faster                                                 |
| scimark_monte_carlo        | 67.4 ms                                                | 66.2 ms: 1.02x faster                                                 |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.02x faster                                                  |
| deltablue                  | 3.23 ms                                                | 3.17 ms: 1.02x faster                                                 |
| float                      | 79.2 ms                                                | 77.9 ms: 1.02x faster                                                 |
| typing_runtime_protocols   | 165 us                                                 | 162 us: 1.02x faster                                                  |
| json                       | 5.36 ms                                                | 5.28 ms: 1.02x faster                                                 |
| sympy_str                  | 275 ms                                                 | 271 ms: 1.01x faster                                                  |
| crypto_pyaes               | 75.3 ms                                                | 74.4 ms: 1.01x faster                                                 |
| scimark_lu                 | 113 ms                                                 | 111 ms: 1.01x faster                                                  |
| sqlglot_transpile          | 1.58 ms                                                | 1.57 ms: 1.01x faster                                                 |
| sqlglot_optimize           | 53.7 ms                                                | 53.1 ms: 1.01x faster                                                 |
| pyflate                    | 471 ms                                                 | 466 ms: 1.01x faster                                                  |
| sympy_integrate            | 19.9 ms                                                | 19.7 ms: 1.01x faster                                                 |
| sqlglot_normalize          | 108 ms                                                 | 107 ms: 1.01x faster                                                  |
| xml_etree_generate         | 86.7 ms                                                | 86.3 ms: 1.00x faster                                                 |
| mako                       | 11.1 ms                                                | 11.1 ms: 1.00x faster                                                 |
| mdp                        | 2.72 sec                                               | 2.71 sec: 1.00x faster                                                |
| chaos                      | 58.1 ms                                                | 58.3 ms: 1.00x slower                                                 |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                  |
| bpe_tokeniser              | 4.75 sec                                               | 4.77 sec: 1.01x slower                                                |
| html5lib                   | 64.2 ms                                                | 64.5 ms: 1.01x slower                                                 |
| pprint_pformat             | 1.49 sec                                               | 1.50 sec: 1.01x slower                                                |
| coroutines                 | 22.7 ms                                                | 22.9 ms: 1.01x slower                                                 |
| pprint_safe_repr           | 728 ms                                                 | 736 ms: 1.01x slower                                                  |
| asyncio_websockets         | 552 ms                                                 | 558 ms: 1.01x slower                                                  |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.01x slower                                                 |
| python_startup_no_site     | 6.96 ms                                                | 7.06 ms: 1.01x slower                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 104 ms: 1.03x slower                                                  |
| async_tree_io_tg           | 857 ms                                                 | 885 ms: 1.03x slower                                                  |
| docutils                   | 2.59 sec                                               | 2.70 sec: 1.04x slower                                                |
| json_loads                 | 27.2 us                                                | 28.5 us: 1.05x slower                                                 |
| async_tree_io              | 842 ms                                                 | 901 ms: 1.07x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (14): sympy_expand, spectral_norm, coverage, async_generators, bench_mp_pool, hexiom, fannkuch, sqlglot_parse, scimark_sor, sympy_sum, regex_dna, nqueens, xml_etree_parse, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dulwich_log, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240815-3.14.0a0-e913d2c/bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.037x faster
# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x