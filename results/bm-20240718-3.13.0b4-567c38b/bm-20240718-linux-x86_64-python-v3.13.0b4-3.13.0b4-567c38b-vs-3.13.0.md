# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b4
- machine: linux-x86_64
- commit hash: 567c38b
- commit date: 2024-07-18
- overall geometric mean: 1.010x faster
- HPT reliability: 57.77%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 265 ms: 1.01x faster                                       |
| docutils       | 2.59 sec                                               | 2.75 sec: 1.06x slower                                     |
| html5lib       | 64.2 ms                                                | 67.1 ms: 1.05x slower                                      |
| tornado_http   | 92.4 ms                                                | 91.7 ms: 1.01x faster                                      |
| Geometric mean | (ref)                                                  | 1.02x slower                                               |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 429 ms: 1.08x faster                                       |
| async_generators           | 436 ms                                                 | 432 ms: 1.01x faster                                       |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                       |
| async_tree_none_tg         | 321 ms                                                 | 325 ms: 1.01x slower                                       |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 595 ms: 1.03x slower                                       |
| async_tree_none            | 351 ms                                                 | 366 ms: 1.04x slower                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 570 ms: 1.04x slower                                       |
| async_tree_io_tg           | 857 ms                                                 | 901 ms: 1.05x slower                                       |
| async_tree_io              | 842 ms                                                 | 902 ms: 1.07x slower                                       |
| Geometric mean             | (ref)                                                  | 1.02x slower                                               |

Benchmark hidden because not significant (2): coroutines, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 79.2 ms                                                | 76.8 ms: 1.03x faster                                      |
| nbody          | 87.0 ms                                                | 85.6 ms: 1.02x faster                                      |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x slower                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.2 ms: 1.04x faster                                      |
| regex_compile  | 132 ms                                                 | 132 ms: 1.00x faster                                       |
| regex_effbot   | 3.73 ms                                                | 3.77 ms: 1.01x slower                                      |
| regex_dna      | 218 ms                                                 | 232 ms: 1.06x slower                                       |
| Geometric mean | (ref)                                                  | 1.01x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|---------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python  | 310 us                                                 | 303 us: 1.02x faster                                       |
| xml_etree_process   | 60.6 ms                                                | 60.9 ms: 1.00x slower                                      |
| xml_etree_generate  | 86.7 ms                                                | 87.3 ms: 1.01x slower                                      |
| xml_etree_parse     | 156 ms                                                 | 158 ms: 1.01x slower                                       |
| json_loads          | 27.2 us                                                | 27.9 us: 1.03x slower                                      |
| xml_etree_iterparse | 101 ms                                                 | 105 ms: 1.04x slower                                       |
| Geometric mean      | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (3): json_dumps, tomli_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.18x faster                                      |
| python_startup_no_site | 6.96 ms                                                | 7.10 ms: 1.02x slower                                      |
| Geometric mean         | (ref)                                                  | 1.08x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| django_template | 35.2 ms                                                | 34.1 ms: 1.03x faster                                      |
| genshi_text     | 23.5 ms                                                | 23.1 ms: 1.02x faster                                      |
| mako            | 11.1 ms                                                | 11.0 ms: 1.01x faster                                      |
| Geometric mean  | (ref)                                                  | 1.01x faster                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mypy2                      | 1.04 sec                                               | 717 ms: 1.45x faster                                       |
| create_gc_cycles           | 2.41 ms                                                | 1.78 ms: 1.35x faster                                      |
| python_startup             | 12.5 ms                                                | 10.5 ms: 1.18x faster                                      |
| gc_traversal               | 4.37 ms                                                | 3.74 ms: 1.17x faster                                      |
| async_tree_memoization_tg  | 464 ms                                                 | 429 ms: 1.08x faster                                       |
| json                       | 5.36 ms                                                | 5.01 ms: 1.07x faster                                      |
| regex_v8                   | 26.2 ms                                                | 25.2 ms: 1.04x faster                                      |
| typing_runtime_protocols   | 165 us                                                 | 159 us: 1.04x faster                                       |
| pathlib                    | 17.5 ms                                                | 17.0 ms: 1.03x faster                                      |
| django_template            | 35.2 ms                                                | 34.1 ms: 1.03x faster                                      |
| float                      | 79.2 ms                                                | 76.8 ms: 1.03x faster                                      |
| logging_format             | 6.40 us                                                | 6.23 us: 1.03x faster                                      |
| telco                      | 8.54 ms                                                | 8.34 ms: 1.02x faster                                      |
| pickle_pure_python         | 310 us                                                 | 303 us: 1.02x faster                                       |
| go                         | 144 ms                                                 | 141 ms: 1.02x faster                                       |
| mdp                        | 2.72 sec                                               | 2.67 sec: 1.02x faster                                     |
| genshi_text                | 23.5 ms                                                | 23.1 ms: 1.02x faster                                      |
| deepcopy_memo              | 39.1 us                                                | 38.5 us: 1.02x faster                                      |
| nbody                      | 87.0 ms                                                | 85.6 ms: 1.02x faster                                      |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.02x faster                                     |
| logging_simple             | 5.72 us                                                | 5.64 us: 1.01x faster                                      |
| richards                   | 48.7 ms                                                | 48.0 ms: 1.01x faster                                      |
| pprint_pformat             | 1.49 sec                                               | 1.47 sec: 1.01x faster                                     |
| raytrace                   | 267 ms                                                 | 264 ms: 1.01x faster                                       |
| thrift                     | 809 us                                                 | 799 us: 1.01x faster                                       |
| crypto_pyaes               | 75.3 ms                                                | 74.4 ms: 1.01x faster                                      |
| richards_super             | 54.9 ms                                                | 54.2 ms: 1.01x faster                                      |
| dulwich_log                | 64.3 ms                                                | 63.7 ms: 1.01x faster                                      |
| async_generators           | 436 ms                                                 | 432 ms: 1.01x faster                                       |
| bench_thread_pool          | 822 us                                                 | 814 us: 1.01x faster                                       |
| mako                       | 11.1 ms                                                | 11.0 ms: 1.01x faster                                      |
| sympy_expand               | 463 ms                                                 | 460 ms: 1.01x faster                                       |
| tornado_http               | 92.4 ms                                                | 91.7 ms: 1.01x faster                                      |
| 2to3                       | 267 ms                                                 | 265 ms: 1.01x faster                                       |
| hexiom                     | 6.16 ms                                                | 6.12 ms: 1.01x faster                                      |
| pprint_safe_repr           | 728 ms                                                 | 724 ms: 1.01x faster                                       |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 5.01 ms: 1.01x faster                                      |
| meteor_contest             | 109 ms                                                 | 108 ms: 1.00x faster                                       |
| generators                 | 29.0 ms                                                | 28.8 ms: 1.00x faster                                      |
| deepcopy                   | 358 us                                                 | 357 us: 1.00x faster                                       |
| regex_compile              | 132 ms                                                 | 132 ms: 1.00x faster                                       |
| spectral_norm              | 115 ms                                                 | 115 ms: 1.00x faster                                       |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x slower                                       |
| sympy_integrate            | 19.9 ms                                                | 19.9 ms: 1.00x slower                                      |
| xml_etree_process          | 60.6 ms                                                | 60.9 ms: 1.00x slower                                      |
| sympy_sum                  | 150 ms                                                 | 151 ms: 1.01x slower                                       |
| deltablue                  | 3.23 ms                                                | 3.25 ms: 1.01x slower                                      |
| nqueens                    | 78.4 ms                                                | 78.9 ms: 1.01x slower                                      |
| xml_etree_generate         | 86.7 ms                                                | 87.3 ms: 1.01x slower                                      |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                       |
| sqlglot_parse              | 1.27 ms                                                | 1.29 ms: 1.01x slower                                      |
| regex_effbot               | 3.73 ms                                                | 3.77 ms: 1.01x slower                                      |
| async_tree_none_tg         | 321 ms                                                 | 325 ms: 1.01x slower                                       |
| xml_etree_parse            | 156 ms                                                 | 158 ms: 1.01x slower                                       |
| scimark_fft                | 364 ms                                                 | 370 ms: 1.02x slower                                       |
| python_startup_no_site     | 6.96 ms                                                | 7.10 ms: 1.02x slower                                      |
| pyflate                    | 471 ms                                                 | 481 ms: 1.02x slower                                       |
| chaos                      | 58.1 ms                                                | 59.5 ms: 1.02x slower                                      |
| scimark_monte_carlo        | 67.4 ms                                                | 69.1 ms: 1.02x slower                                      |
| logging_silent             | 102 ns                                                 | 104 ns: 1.02x slower                                       |
| json_loads                 | 27.2 us                                                | 27.9 us: 1.03x slower                                      |
| scimark_lu                 | 113 ms                                                 | 116 ms: 1.03x slower                                       |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 595 ms: 1.03x slower                                       |
| xml_etree_iterparse        | 101 ms                                                 | 105 ms: 1.04x slower                                       |
| async_tree_none            | 351 ms                                                 | 366 ms: 1.04x slower                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 570 ms: 1.04x slower                                       |
| bpe_tokeniser              | 4.75 sec                                               | 4.96 sec: 1.05x slower                                     |
| html5lib                   | 64.2 ms                                                | 67.1 ms: 1.05x slower                                      |
| async_tree_io_tg           | 857 ms                                                 | 901 ms: 1.05x slower                                       |
| docutils                   | 2.59 sec                                               | 2.75 sec: 1.06x slower                                     |
| scimark_sor                | 124 ms                                                 | 131 ms: 1.06x slower                                       |
| regex_dna                  | 218 ms                                                 | 232 ms: 1.06x slower                                       |
| async_tree_io              | 842 ms                                                 | 902 ms: 1.07x slower                                       |
| coverage                   | 84.0 ms                                                | 91.7 ms: 1.09x slower                                      |
| Geometric mean             | (ref)                                                  | 1.01x faster                                               |

Benchmark hidden because not significant (16): pylint, fannkuch, sympy_str, genshi_xml, json_dumps, tomli_loads, coroutines, sqlglot_normalize, sqlglot_transpile, sqlglot_optimize, unpickle_pure_python, bench_mp_pool, comprehensions, chameleon, deepcopy_reduce, async_tree_memoization
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (3) of results/bm-20240718-3.13.0b4-567c38b/bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b.json: asyncio_tcp, asyncio_tcp_ssl, dask

- Geometric mean (including insignificant results): 1.010x faster
# HPT report

- Reliability score: 57.77% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x