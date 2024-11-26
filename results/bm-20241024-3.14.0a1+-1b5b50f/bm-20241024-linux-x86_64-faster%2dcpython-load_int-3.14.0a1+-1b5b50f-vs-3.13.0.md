# Results vs. 3.13.0

- fork: faster-cpython
- ref: load_int
- machine: linux-x86_64
- commit hash: 1b5b50f
- commit date: 2024-10-24
- overall geometric mean: 1.017x faster
- HPT reliability: 95.52%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 254 ms: 1.05x faster                                                 |
| docutils       | 2.59 sec                                               | 2.67 sec: 1.03x slower                                               |
| html5lib       | 64.2 ms                                                | 63.1 ms: 1.02x faster                                                |
| tornado_http   | 92.4 ms                                                | 90.1 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 384 ms: 1.21x faster                                                 |
| async_tree_none            | 351 ms                                                 | 328 ms: 1.07x faster                                                 |
| async_tree_memoization     | 442 ms                                                 | 413 ms: 1.07x faster                                                 |
| async_generators           | 436 ms                                                 | 433 ms: 1.01x faster                                                 |
| asyncio_websockets         | 552 ms                                                 | 556 ms: 1.01x slower                                                 |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 564 ms: 1.03x slower                                                 |
| coroutines                 | 22.7 ms                                                | 23.6 ms: 1.04x slower                                                |
| async_tree_io_tg           | 857 ms                                                 | 982 ms: 1.15x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_io, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                 |
| nbody          | 87.0 ms                                                | 96.0 ms: 1.10x slower                                                |
| Geometric mean | (ref)                                                  | 1.04x slower                                                         |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.0 ms: 1.05x faster                                                |
| regex_effbot   | 3.73 ms                                                | 3.61 ms: 1.03x faster                                                |
| regex_compile  | 132 ms                                                 | 129 ms: 1.03x faster                                                 |
| regex_dna      | 218 ms                                                 | 216 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|---------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| json_loads          | 27.2 us                                                | 26.1 us: 1.04x faster                                                |
| tomli_loads         | 2.14 sec                                               | 2.08 sec: 1.03x faster                                               |
| xml_etree_process   | 60.6 ms                                                | 59.9 ms: 1.01x faster                                                |
| xml_etree_generate  | 86.7 ms                                                | 86.1 ms: 1.01x faster                                                |
| xml_etree_parse     | 156 ms                                                 | 158 ms: 1.01x slower                                                 |
| xml_etree_iterparse | 101 ms                                                 | 107 ms: 1.05x slower                                                 |
| json_dumps          | 10.6 ms                                                | 11.4 ms: 1.08x slower                                                |
| Geometric mean      | (ref)                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (2): unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 11.7 ms: 1.06x faster                                                |
| python_startup_no_site | 6.96 ms                                                | 7.02 ms: 1.01x slower                                                |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 23.2 ms: 1.01x faster                                                |
| django_template | 35.2 ms                                                | 34.8 ms: 1.01x faster                                                |
| genshi_xml      | 50.9 ms                                                | 52.1 ms: 1.02x slower                                                |
| mako            | 11.1 ms                                                | 11.5 ms: 1.04x slower                                                |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 261 us: 1.37x faster                                                 |
| deepcopy_memo              | 39.1 us                                                | 30.8 us: 1.27x faster                                                |
| async_tree_memoization_tg  | 464 ms                                                 | 384 ms: 1.21x faster                                                 |
| go                         | 144 ms                                                 | 121 ms: 1.19x faster                                                 |
| deepcopy_reduce            | 3.20 us                                                | 2.70 us: 1.18x faster                                                |
| json                       | 5.36 ms                                                | 4.83 ms: 1.11x faster                                                |
| mdp                        | 2.72 sec                                               | 2.51 sec: 1.09x faster                                               |
| pathlib                    | 17.5 ms                                                | 16.2 ms: 1.08x faster                                                |
| async_tree_none            | 351 ms                                                 | 328 ms: 1.07x faster                                                 |
| async_tree_memoization     | 442 ms                                                 | 413 ms: 1.07x faster                                                 |
| python_startup             | 12.5 ms                                                | 11.7 ms: 1.06x faster                                                |
| telco                      | 8.54 ms                                                | 8.04 ms: 1.06x faster                                                |
| pyflate                    | 471 ms                                                 | 446 ms: 1.06x faster                                                 |
| 2to3                       | 267 ms                                                 | 254 ms: 1.05x faster                                                 |
| regex_v8                   | 26.2 ms                                                | 25.0 ms: 1.05x faster                                                |
| logging_format             | 6.40 us                                                | 6.11 us: 1.05x faster                                                |
| json_loads                 | 27.2 us                                                | 26.1 us: 1.04x faster                                                |
| sqlalchemy_declarative     | 133 ms                                                 | 128 ms: 1.04x faster                                                 |
| richards_super             | 54.9 ms                                                | 52.7 ms: 1.04x faster                                                |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.84 ms: 1.04x faster                                                |
| thrift                     | 809 us                                                 | 780 us: 1.04x faster                                                 |
| richards                   | 48.7 ms                                                | 46.9 ms: 1.04x faster                                                |
| regex_effbot               | 3.73 ms                                                | 3.61 ms: 1.03x faster                                                |
| sympy_str                  | 275 ms                                                 | 267 ms: 1.03x faster                                                 |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.03x faster                                               |
| typing_runtime_protocols   | 165 us                                                 | 160 us: 1.03x faster                                                 |
| tomli_loads                | 2.14 sec                                               | 2.08 sec: 1.03x faster                                               |
| regex_compile              | 132 ms                                                 | 129 ms: 1.03x faster                                                 |
| tornado_http               | 92.4 ms                                                | 90.1 ms: 1.03x faster                                                |
| meteor_contest             | 109 ms                                                 | 106 ms: 1.03x faster                                                 |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                                 |
| generators                 | 29.0 ms                                                | 28.3 ms: 1.02x faster                                                |
| crypto_pyaes               | 75.3 ms                                                | 73.6 ms: 1.02x faster                                                |
| logging_simple             | 5.72 us                                                | 5.59 us: 1.02x faster                                                |
| sympy_expand               | 463 ms                                                 | 455 ms: 1.02x faster                                                 |
| scimark_fft                | 364 ms                                                 | 358 ms: 1.02x faster                                                 |
| html5lib                   | 64.2 ms                                                | 63.1 ms: 1.02x faster                                                |
| genshi_text                | 23.5 ms                                                | 23.2 ms: 1.01x faster                                                |
| xml_etree_process          | 60.6 ms                                                | 59.9 ms: 1.01x faster                                                |
| regex_dna                  | 218 ms                                                 | 216 ms: 1.01x faster                                                 |
| sqlglot_normalize          | 108 ms                                                 | 106 ms: 1.01x faster                                                 |
| django_template            | 35.2 ms                                                | 34.8 ms: 1.01x faster                                                |
| xml_etree_generate         | 86.7 ms                                                | 86.1 ms: 1.01x faster                                                |
| sqlglot_optimize           | 53.7 ms                                                | 53.3 ms: 1.01x faster                                                |
| dulwich_log                | 64.3 ms                                                | 63.9 ms: 1.01x faster                                                |
| async_generators           | 436 ms                                                 | 433 ms: 1.01x faster                                                 |
| coverage                   | 84.0 ms                                                | 83.6 ms: 1.00x faster                                                |
| sqlglot_transpile          | 1.58 ms                                                | 1.59 ms: 1.01x slower                                                |
| pidigits                   | 186 ms                                                 | 187 ms: 1.01x slower                                                 |
| scimark_sor                | 124 ms                                                 | 124 ms: 1.01x slower                                                 |
| asyncio_websockets         | 552 ms                                                 | 556 ms: 1.01x slower                                                 |
| python_startup_no_site     | 6.96 ms                                                | 7.02 ms: 1.01x slower                                                |
| logging_silent             | 102 ns                                                 | 103 ns: 1.01x slower                                                 |
| sqlglot_parse              | 1.27 ms                                                | 1.29 ms: 1.01x slower                                                |
| xml_etree_parse            | 156 ms                                                 | 158 ms: 1.01x slower                                                 |
| scimark_monte_carlo        | 67.4 ms                                                | 68.4 ms: 1.01x slower                                                |
| nqueens                    | 78.4 ms                                                | 79.7 ms: 1.02x slower                                                |
| bench_thread_pool          | 822 us                                                 | 837 us: 1.02x slower                                                 |
| hexiom                     | 6.16 ms                                                | 6.29 ms: 1.02x slower                                                |
| raytrace                   | 267 ms                                                 | 273 ms: 1.02x slower                                                 |
| deltablue                  | 3.23 ms                                                | 3.30 ms: 1.02x slower                                                |
| genshi_xml                 | 50.9 ms                                                | 52.1 ms: 1.02x slower                                                |
| comprehensions             | 16.5 us                                                | 16.9 us: 1.02x slower                                                |
| docutils                   | 2.59 sec                                               | 2.67 sec: 1.03x slower                                               |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 564 ms: 1.03x slower                                                 |
| mako                       | 11.1 ms                                                | 11.5 ms: 1.04x slower                                                |
| coroutines                 | 22.7 ms                                                | 23.6 ms: 1.04x slower                                                |
| chaos                      | 58.1 ms                                                | 60.8 ms: 1.05x slower                                                |
| xml_etree_iterparse        | 101 ms                                                 | 107 ms: 1.05x slower                                                 |
| gc_traversal               | 4.37 ms                                                | 4.70 ms: 1.08x slower                                                |
| json_dumps                 | 10.6 ms                                                | 11.4 ms: 1.08x slower                                                |
| nbody                      | 87.0 ms                                                | 96.0 ms: 1.10x slower                                                |
| create_gc_cycles           | 2.41 ms                                                | 2.66 ms: 1.11x slower                                                |
| async_tree_io_tg           | 857 ms                                                 | 982 ms: 1.15x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 77.8 ms: 3.24x slower                                                |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (16): sqlalchemy_imperative, async_tree_cpu_io_mixed, async_tree_io, sympy_integrate, scimark_lu, spectral_norm, unpickle_pure_python, pprint_safe_repr, pickle_pure_python, pprint_pformat, float, bpe_tokeniser, fannkuch, async_tree_none_tg, sphinx, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path

- Geometric mean (including insignificant results): 1.017x faster
# HPT report

- Reliability score: 95.52% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x