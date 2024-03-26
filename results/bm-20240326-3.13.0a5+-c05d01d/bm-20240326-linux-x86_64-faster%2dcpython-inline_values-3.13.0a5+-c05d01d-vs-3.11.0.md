# Results vs. 3.11.0

- fork: faster-cpython
- ref: inline_values
- machine: linux-x86_64
- commit hash: c05d01d
- commit date: 2024-03-26
- overall geometric mean: 1.08x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240326-linux-x86_64-faster%2dcpython-inline_values-3.13.0a5+-c05d01d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 264 ms                                                 | 268 ms: 1.02x slower                                                      |
| chameleon      | 6.70 ms                                                | 6.88 ms: 1.03x slower                                                     |
| docutils       | 2.66 sec                                               | 2.78 sec: 1.04x slower                                                    |
| html5lib       | 64.8 ms                                                | 66.1 ms: 1.02x slower                                                     |
| tornado_http   | 98.1 ms                                                | 94.2 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240326-linux-x86_64-faster%2dcpython-inline_values-3.13.0a5+-c05d01d |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 626 ms                                                 | 440 ms: 1.42x faster                                                      |
| async_tree_io_tg           | 1.29 sec                                               | 914 ms: 1.42x faster                                                      |
| async_tree_none_tg         | 491 ms                                                 | 347 ms: 1.41x faster                                                      |
| async_tree_none            | 528 ms                                                 | 376 ms: 1.40x faster                                                      |
| async_tree_memoization     | 639 ms                                                 | 463 ms: 1.38x faster                                                      |
| async_tree_io              | 1.29 sec                                               | 936 ms: 1.37x faster                                                      |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 611 ms: 1.25x faster                                                      |
| async_tree_cpu_io_mixed    | 749 ms                                                 | 609 ms: 1.23x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.36x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240326-linux-x86_64-faster%2dcpython-inline_values-3.13.0a5+-c05d01d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 96.0 ms                                                | 89.3 ms: 1.07x faster                                                     |
| float          | 78.9 ms                                                | 78.1 ms: 1.01x faster                                                     |
| pidigits       | 194 ms                                                 | 194 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240326-linux-x86_64-faster%2dcpython-inline_values-3.13.0a5+-c05d01d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 141 ms                                                 | 133 ms: 1.06x faster                                                      |
| regex_effbot   | 3.51 ms                                                | 3.72 ms: 1.06x slower                                                     |
| regex_dna      | 205 ms                                                 | 221 ms: 1.08x slower                                                      |
| regex_v8       | 22.9 ms                                                | 25.5 ms: 1.11x slower                                                     |
| Geometric mean | (ref)                                                  | 1.05x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240326-linux-x86_64-faster%2dcpython-inline_values-3.13.0a5+-c05d01d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 13.3 ms                                                | 10.5 ms: 1.27x faster                                                     |
| unpickle_pure_python | 242 us                                                 | 216 us: 1.12x faster                                                      |
| pickle_pure_python   | 320 us                                                 | 298 us: 1.07x faster                                                      |
| tomli_loads          | 2.30 sec                                               | 2.18 sec: 1.06x faster                                                    |
| json_loads           | 29.2 us                                                | 28.6 us: 1.02x faster                                                     |
| unpickle_list        | 5.21 us                                                | 5.25 us: 1.01x slower                                                     |
| xml_etree_process    | 56.9 ms                                                | 59.8 ms: 1.05x slower                                                     |
| xml_etree_generate   | 81.1 ms                                                | 86.6 ms: 1.07x slower                                                     |
| pickle               | 11.0 us                                                | 11.8 us: 1.07x slower                                                     |
| pickle_list          | 4.59 us                                                | 5.25 us: 1.14x slower                                                     |
| unpickle             | 13.8 us                                                | 16.2 us: 1.17x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_iterparse, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240326-linux-x86_64-faster%2dcpython-inline_values-3.13.0a5+-c05d01d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 8.56 ms                                                | 10.5 ms: 1.23x slower                                                     |
| python_startup_no_site | 6.01 ms                                                | 8.87 ms: 1.48x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.35x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240326-linux-x86_64-faster%2dcpython-inline_values-3.13.0a5+-c05d01d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_xml     | 53.4 ms                                                | 53.2 ms: 1.00x faster                                                     |
| mako           | 10.7 ms                                                | 10.8 ms: 1.01x slower                                                     |
| genshi_text    | 22.5 ms                                                | 24.3 ms: 1.08x slower                                                     |
| Geometric mean | (ref)                                                  | 1.03x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240326-linux-x86_64-faster%2dcpython-inline_values-3.13.0a5+-c05d01d |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols   | 520 us                                                 | 111 us: 4.69x faster                                                      |
| generators                 | 74.9 ms                                                | 29.7 ms: 2.52x faster                                                     |
| asyncio_tcp                | 875 ms                                                 | 513 ms: 1.71x faster                                                      |
| asyncio_tcp_ssl            | 3.11 sec                                               | 1.84 sec: 1.69x faster                                                    |
| pylint                     | 476 ms                                                 | 321 ms: 1.48x faster                                                      |
| comprehensions             | 23.6 us                                                | 16.4 us: 1.44x faster                                                     |
| async_tree_memoization_tg  | 626 ms                                                 | 440 ms: 1.42x faster                                                      |
| async_tree_io_tg           | 1.29 sec                                               | 914 ms: 1.42x faster                                                      |
| async_tree_none_tg         | 491 ms                                                 | 347 ms: 1.41x faster                                                      |
| async_tree_none            | 528 ms                                                 | 376 ms: 1.40x faster                                                      |
| async_tree_memoization     | 639 ms                                                 | 463 ms: 1.38x faster                                                      |
| async_tree_io              | 1.29 sec                                               | 936 ms: 1.37x faster                                                      |
| json_dumps                 | 13.3 ms                                                | 10.5 ms: 1.27x faster                                                     |
| deltablue                  | 3.92 ms                                                | 3.12 ms: 1.26x faster                                                     |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 611 ms: 1.25x faster                                                      |
| async_tree_cpu_io_mixed    | 749 ms                                                 | 609 ms: 1.23x faster                                                      |
| coroutines                 | 27.0 ms                                                | 22.3 ms: 1.21x faster                                                     |
| chaos                      | 71.9 ms                                                | 59.3 ms: 1.21x faster                                                     |
| raytrace                   | 309 ms                                                 | 257 ms: 1.20x faster                                                      |
| richards_super             | 61.9 ms                                                | 51.7 ms: 1.20x faster                                                     |
| sqlglot_parse              | 1.43 ms                                                | 1.26 ms: 1.14x faster                                                     |
| hexiom                     | 6.89 ms                                                | 6.10 ms: 1.13x faster                                                     |
| logging_silent             | 111 ns                                                 | 98.5 ns: 1.13x faster                                                     |
| unpickle_pure_python       | 242 us                                                 | 216 us: 1.12x faster                                                      |
| sqlglot_transpile          | 1.75 ms                                                | 1.57 ms: 1.12x faster                                                     |
| sympy_sum                  | 169 ms                                                 | 154 ms: 1.10x faster                                                      |
| gc_traversal               | 4.01 ms                                                | 3.67 ms: 1.09x faster                                                     |
| richards                   | 49.8 ms                                                | 45.7 ms: 1.09x faster                                                     |
| crypto_pyaes               | 76.7 ms                                                | 71.0 ms: 1.08x faster                                                     |
| scimark_monte_carlo        | 70.7 ms                                                | 65.5 ms: 1.08x faster                                                     |
| deepcopy_memo              | 40.2 us                                                | 37.2 us: 1.08x faster                                                     |
| nqueens                    | 87.9 ms                                                | 81.6 ms: 1.08x faster                                                     |
| nbody                      | 96.0 ms                                                | 89.3 ms: 1.07x faster                                                     |
| sympy_str                  | 297 ms                                                 | 277 ms: 1.07x faster                                                      |
| pickle_pure_python         | 320 us                                                 | 298 us: 1.07x faster                                                      |
| go                         | 149 ms                                                 | 139 ms: 1.07x faster                                                      |
| sympy_integrate            | 21.5 ms                                                | 20.1 ms: 1.07x faster                                                     |
| scimark_lu                 | 116 ms                                                 | 110 ms: 1.06x faster                                                      |
| regex_compile              | 141 ms                                                 | 133 ms: 1.06x faster                                                      |
| logging_simple             | 6.22 us                                                | 5.87 us: 1.06x faster                                                     |
| tomli_loads                | 2.30 sec                                               | 2.18 sec: 1.06x faster                                                    |
| mdp                        | 2.77 sec                                               | 2.63 sec: 1.06x faster                                                    |
| logging_format             | 6.81 us                                                | 6.48 us: 1.05x faster                                                     |
| pycparser                  | 1.19 sec                                               | 1.13 sec: 1.05x faster                                                    |
| deepcopy                   | 365 us                                                 | 349 us: 1.05x faster                                                      |
| sympy_expand               | 484 ms                                                 | 463 ms: 1.05x faster                                                      |
| fannkuch                   | 405 ms                                                 | 389 ms: 1.04x faster                                                      |
| tornado_http               | 98.1 ms                                                | 94.2 ms: 1.04x faster                                                     |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.84 ms: 1.04x faster                                                     |
| sqlglot_normalize          | 113 ms                                                 | 109 ms: 1.03x faster                                                      |
| pprint_pformat             | 1.55 sec                                               | 1.51 sec: 1.03x faster                                                    |
| scimark_sor                | 121 ms                                                 | 119 ms: 1.02x faster                                                      |
| json_loads                 | 29.2 us                                                | 28.6 us: 1.02x faster                                                     |
| deepcopy_reduce            | 3.22 us                                                | 3.17 us: 1.01x faster                                                     |
| meteor_contest             | 109 ms                                                 | 108 ms: 1.01x faster                                                      |
| pprint_safe_repr           | 747 ms                                                 | 739 ms: 1.01x faster                                                      |
| float                      | 78.9 ms                                                | 78.1 ms: 1.01x faster                                                     |
| bench_thread_pool          | 834 us                                                 | 826 us: 1.01x faster                                                      |
| bench_mp_pool              | 24.0 ms                                                | 23.8 ms: 1.01x faster                                                     |
| sqlglot_optimize           | 55.3 ms                                                | 54.8 ms: 1.01x faster                                                     |
| genshi_xml                 | 53.4 ms                                                | 53.2 ms: 1.00x faster                                                     |
| pidigits                   | 194 ms                                                 | 194 ms: 1.00x faster                                                      |
| unpickle_list              | 5.21 us                                                | 5.25 us: 1.01x slower                                                     |
| pathlib                    | 18.5 ms                                                | 18.6 ms: 1.01x slower                                                     |
| mako                       | 10.7 ms                                                | 10.8 ms: 1.01x slower                                                     |
| 2to3                       | 264 ms                                                 | 268 ms: 1.02x slower                                                      |
| html5lib                   | 64.8 ms                                                | 66.1 ms: 1.02x slower                                                     |
| spectral_norm              | 108 ms                                                 | 111 ms: 1.02x slower                                                      |
| scimark_fft                | 345 ms                                                 | 354 ms: 1.03x slower                                                      |
| chameleon                  | 6.70 ms                                                | 6.88 ms: 1.03x slower                                                     |
| thrift                     | 784 us                                                 | 808 us: 1.03x slower                                                      |
| asyncio_websockets         | 550 ms                                                 | 569 ms: 1.03x slower                                                      |
| pyflate                    | 434 ms                                                 | 451 ms: 1.04x slower                                                      |
| docutils                   | 2.66 sec                                               | 2.78 sec: 1.04x slower                                                    |
| json                       | 5.24 ms                                                | 5.47 ms: 1.04x slower                                                     |
| dulwich_log                | 64.6 ms                                                | 67.7 ms: 1.05x slower                                                     |
| unpack_sequence            | 43.5 ns                                                | 45.6 ns: 1.05x slower                                                     |
| xml_etree_process          | 56.9 ms                                                | 59.8 ms: 1.05x slower                                                     |
| aiohttp                    | 1.12 ms                                                | 1.18 ms: 1.05x slower                                                     |
| regex_effbot               | 3.51 ms                                                | 3.72 ms: 1.06x slower                                                     |
| gunicorn                   | 1.20 ms                                                | 1.28 ms: 1.06x slower                                                     |
| create_gc_cycles           | 1.43 ms                                                | 1.53 ms: 1.07x slower                                                     |
| xml_etree_generate         | 81.1 ms                                                | 86.6 ms: 1.07x slower                                                     |
| pickle                     | 11.0 us                                                | 11.8 us: 1.07x slower                                                     |
| mypy2                      | 686 ms                                                 | 737 ms: 1.07x slower                                                      |
| genshi_text                | 22.5 ms                                                | 24.3 ms: 1.08x slower                                                     |
| regex_dna                  | 205 ms                                                 | 221 ms: 1.08x slower                                                      |
| regex_v8                   | 22.9 ms                                                | 25.5 ms: 1.11x slower                                                     |
| sqlite_synth               | 2.57 us                                                | 2.92 us: 1.13x slower                                                     |
| pickle_list                | 4.59 us                                                | 5.25 us: 1.14x slower                                                     |
| unpickle                   | 13.8 us                                                | 16.2 us: 1.17x slower                                                     |
| async_generators           | 374 ms                                                 | 446 ms: 1.19x slower                                                      |
| python_startup             | 8.56 ms                                                | 10.5 ms: 1.23x slower                                                     |
| telco                      | 6.86 ms                                                | 8.50 ms: 1.24x slower                                                     |
| coverage                   | 78.8 ms                                                | 98.3 ms: 1.25x slower                                                     |
| python_startup_no_site     | 6.01 ms                                                | 8.87 ms: 1.48x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                              |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_iterparse, pickle_dict, dask
Ignored benchmarks (5) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: django_template, djangocms, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x


# Memory

- memory change: 1.01x