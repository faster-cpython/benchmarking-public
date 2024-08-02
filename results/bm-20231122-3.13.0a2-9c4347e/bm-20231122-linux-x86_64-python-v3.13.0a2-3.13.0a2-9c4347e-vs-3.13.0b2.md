# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a2
- machine: linux-x86_64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.02x slower
- HPT reliability: 75.04%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.95x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 272 ms: 1.01x faster                                       |
| chameleon      | 7.22 ms                                                    | 6.93 ms: 1.04x faster                                      |
| docutils       | 2.83 sec                                                   | 2.69 sec: 1.05x faster                                     |
| html5lib       | 67.2 ms                                                    | 66.3 ms: 1.01x faster                                      |
| tornado_http   | 94.6 ms                                                    | 97.6 ms: 1.03x slower                                      |
| Geometric mean | (ref)                                                      | 1.02x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 451 ms: 1.19x slower                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 733 ms: 1.20x slower                                       |
| async_tree_memoization     | 463 ms                                                     | 583 ms: 1.26x slower                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 760 ms: 1.29x slower                                       |
| async_tree_io              | 939 ms                                                     | 1.22 sec: 1.30x slower                                     |
| async_tree_io_tg           | 936 ms                                                     | 1.26 sec: 1.35x slower                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 618 ms: 1.39x slower                                       |
| async_tree_none_tg         | 336 ms                                                     | 471 ms: 1.40x slower                                       |
| Geometric mean             | (ref)                                                      | 1.30x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 91.0 ms: 1.03x slower                                      |
| pidigits       | 191 ms                                                     | 197 ms: 1.03x slower                                       |
| float          | 78.9 ms                                                    | 83.5 ms: 1.06x slower                                      |
| Geometric mean | (ref)                                                      | 1.04x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                    | 3.57 ms: 1.03x faster                                      |
| regex_dna      | 221 ms                                                     | 219 ms: 1.01x faster                                       |
| regex_compile  | 137 ms                                                     | 137 ms: 1.00x slower                                       |
| Geometric mean | (ref)                                                      | 1.01x faster                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| unpickle_list        | 5.34 us                                                    | 5.12 us: 1.04x faster                                      |
| xml_etree_process    | 61.2 ms                                                    | 60.5 ms: 1.01x faster                                      |
| json_loads           | 28.9 us                                                    | 28.7 us: 1.01x faster                                      |
| json_dumps           | 10.7 ms                                                    | 10.7 ms: 1.01x faster                                      |
| pickle_dict          | 34.8 us                                                    | 34.9 us: 1.00x slower                                      |
| xml_etree_iterparse  | 107 ms                                                     | 108 ms: 1.01x slower                                       |
| xml_etree_generate   | 87.4 ms                                                    | 88.2 ms: 1.01x slower                                      |
| pickle_pure_python   | 305 us                                                     | 313 us: 1.02x slower                                       |
| unpickle_pure_python | 218 us                                                     | 224 us: 1.03x slower                                       |
| pickle               | 11.5 us                                                    | 11.8 us: 1.03x slower                                      |
| unpickle             | 15.1 us                                                    | 15.7 us: 1.04x slower                                      |
| tomli_loads          | 2.12 sec                                                   | 2.23 sec: 1.05x slower                                     |
| Geometric mean       | (ref)                                                      | 1.01x slower                                               |

Benchmark hidden because not significant (2): pickle_list, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.7 ms: 1.01x faster                                      |
| python_startup_no_site | 7.11 ms                                                    | 9.26 ms: 1.30x slower                                      |
| Geometric mean         | (ref)                                                      | 1.14x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 23.8 ms: 1.01x slower                                      |
| genshi_xml      | 51.6 ms                                                    | 52.1 ms: 1.01x slower                                      |
| django_template | 34.8 ms                                                    | 35.2 ms: 1.01x slower                                      |
| mako            | 11.2 ms                                                    | 11.7 ms: 1.04x slower                                      |
| Geometric mean  | (ref)                                                      | 1.02x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols   | 165 us                                                     | 119 us: 1.38x faster                                       |
| create_gc_cycles           | 1.82 ms                                                    | 1.48 ms: 1.22x faster                                      |
| deepcopy_reduce            | 3.35 us                                                    | 3.14 us: 1.07x faster                                      |
| coroutines                 | 23.2 ms                                                    | 21.8 ms: 1.06x faster                                      |
| crypto_pyaes               | 77.5 ms                                                    | 73.3 ms: 1.06x faster                                      |
| mdp                        | 2.79 sec                                                   | 2.64 sec: 1.06x faster                                     |
| docutils                   | 2.83 sec                                                   | 2.69 sec: 1.05x faster                                     |
| scimark_fft                | 392 ms                                                     | 375 ms: 1.05x faster                                       |
| spectral_norm              | 116 ms                                                     | 111 ms: 1.05x faster                                       |
| unpickle_list              | 5.34 us                                                    | 5.12 us: 1.04x faster                                      |
| scimark_lu                 | 122 ms                                                     | 117 ms: 1.04x faster                                       |
| richards_super             | 57.4 ms                                                    | 55.1 ms: 1.04x faster                                      |
| chameleon                  | 7.22 ms                                                    | 6.93 ms: 1.04x faster                                      |
| sqlite_synth               | 2.99 us                                                    | 2.87 us: 1.04x faster                                      |
| deepcopy                   | 367 us                                                     | 354 us: 1.04x faster                                       |
| flaskblogging              | 9.01 ms                                                    | 8.70 ms: 1.04x faster                                      |
| sympy_str                  | 282 ms                                                     | 273 ms: 1.04x faster                                       |
| sqlglot_normalize          | 110 ms                                                     | 107 ms: 1.03x faster                                       |
| sympy_expand               | 473 ms                                                     | 459 ms: 1.03x faster                                       |
| sympy_sum                  | 156 ms                                                     | 151 ms: 1.03x faster                                       |
| regex_effbot               | 3.67 ms                                                    | 3.57 ms: 1.03x faster                                      |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 5.13 ms: 1.03x faster                                      |
| sympy_integrate            | 20.5 ms                                                    | 20.0 ms: 1.03x faster                                      |
| richards                   | 50.9 ms                                                    | 49.7 ms: 1.02x faster                                      |
| sqlglot_optimize           | 55.5 ms                                                    | 54.3 ms: 1.02x faster                                      |
| thrift                     | 823 us                                                     | 805 us: 1.02x faster                                       |
| asyncio_tcp                | 508 ms                                                     | 501 ms: 1.01x faster                                       |
| html5lib                   | 67.2 ms                                                    | 66.3 ms: 1.01x faster                                      |
| pprint_pformat             | 1.56 sec                                                   | 1.54 sec: 1.01x faster                                     |
| json                       | 5.31 ms                                                    | 5.24 ms: 1.01x faster                                      |
| xml_etree_process          | 61.2 ms                                                    | 60.5 ms: 1.01x faster                                      |
| aiohttp                    | 1.18 ms                                                    | 1.17 ms: 1.01x faster                                      |
| scimark_sor                | 127 ms                                                     | 126 ms: 1.01x faster                                       |
| gunicorn                   | 1.28 ms                                                    | 1.27 ms: 1.01x faster                                      |
| 2to3                       | 274 ms                                                     | 272 ms: 1.01x faster                                       |
| regex_dna                  | 221 ms                                                     | 219 ms: 1.01x faster                                       |
| python_startup             | 10.8 ms                                                    | 10.7 ms: 1.01x faster                                      |
| json_loads                 | 28.9 us                                                    | 28.7 us: 1.01x faster                                      |
| pprint_safe_repr           | 758 ms                                                     | 753 ms: 1.01x faster                                       |
| asyncio_websockets         | 567 ms                                                     | 563 ms: 1.01x faster                                       |
| json_dumps                 | 10.7 ms                                                    | 10.7 ms: 1.01x faster                                      |
| sqlglot_parse              | 1.32 ms                                                    | 1.31 ms: 1.00x faster                                      |
| pickle_dict                | 34.8 us                                                    | 34.9 us: 1.00x slower                                      |
| regex_compile              | 137 ms                                                     | 137 ms: 1.00x slower                                       |
| hexiom                     | 6.30 ms                                                    | 6.32 ms: 1.00x slower                                      |
| logging_format             | 6.47 us                                                    | 6.50 us: 1.01x slower                                      |
| meteor_contest             | 110 ms                                                     | 110 ms: 1.01x slower                                       |
| genshi_text                | 23.7 ms                                                    | 23.8 ms: 1.01x slower                                      |
| dulwich_log                | 67.2 ms                                                    | 67.6 ms: 1.01x slower                                      |
| xml_etree_iterparse        | 107 ms                                                     | 108 ms: 1.01x slower                                       |
| xml_etree_generate         | 87.4 ms                                                    | 88.2 ms: 1.01x slower                                      |
| genshi_xml                 | 51.6 ms                                                    | 52.1 ms: 1.01x slower                                      |
| scimark_monte_carlo        | 69.2 ms                                                    | 70.0 ms: 1.01x slower                                      |
| django_template            | 34.8 ms                                                    | 35.2 ms: 1.01x slower                                      |
| telco                      | 8.41 ms                                                    | 8.53 ms: 1.01x slower                                      |
| generators                 | 29.6 ms                                                    | 30.1 ms: 1.02x slower                                      |
| go                         | 145 ms                                                     | 148 ms: 1.02x slower                                       |
| bench_thread_pool          | 834 us                                                     | 852 us: 1.02x slower                                       |
| coverage                   | 93.1 ms                                                    | 95.2 ms: 1.02x slower                                      |
| pickle_pure_python         | 305 us                                                     | 313 us: 1.02x slower                                       |
| logging_simple             | 5.74 us                                                    | 5.89 us: 1.03x slower                                      |
| comprehensions             | 16.6 us                                                    | 17.0 us: 1.03x slower                                      |
| unpickle_pure_python       | 218 us                                                     | 224 us: 1.03x slower                                       |
| nqueens                    | 81.4 ms                                                    | 83.5 ms: 1.03x slower                                      |
| pycparser                  | 1.16 sec                                                   | 1.19 sec: 1.03x slower                                     |
| pickle                     | 11.5 us                                                    | 11.8 us: 1.03x slower                                      |
| nbody                      | 88.3 ms                                                    | 91.0 ms: 1.03x slower                                      |
| tornado_http               | 94.6 ms                                                    | 97.6 ms: 1.03x slower                                      |
| pidigits                   | 191 ms                                                     | 197 ms: 1.03x slower                                       |
| chaos                      | 61.3 ms                                                    | 63.4 ms: 1.03x slower                                      |
| mako                       | 11.2 ms                                                    | 11.7 ms: 1.04x slower                                      |
| unpickle                   | 15.1 us                                                    | 15.7 us: 1.04x slower                                      |
| async_generators           | 442 ms                                                     | 459 ms: 1.04x slower                                       |
| logging_silent             | 105 ns                                                     | 109 ns: 1.04x slower                                       |
| tomli_loads                | 2.12 sec                                                   | 2.23 sec: 1.05x slower                                     |
| deltablue                  | 3.25 ms                                                    | 3.44 ms: 1.06x slower                                      |
| float                      | 78.9 ms                                                    | 83.5 ms: 1.06x slower                                      |
| raytrace                   | 267 ms                                                     | 284 ms: 1.07x slower                                       |
| pathlib                    | 17.3 ms                                                    | 18.6 ms: 1.07x slower                                      |
| gc_traversal               | 3.98 ms                                                    | 4.37 ms: 1.10x slower                                      |
| mypy2                      | 742 ms                                                     | 866 ms: 1.17x slower                                       |
| async_tree_none            | 378 ms                                                     | 451 ms: 1.19x slower                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 733 ms: 1.20x slower                                       |
| async_tree_memoization     | 463 ms                                                     | 583 ms: 1.26x slower                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 760 ms: 1.29x slower                                       |
| async_tree_io              | 939 ms                                                     | 1.22 sec: 1.30x slower                                     |
| python_startup_no_site     | 7.11 ms                                                    | 9.26 ms: 1.30x slower                                      |
| async_tree_io_tg           | 936 ms                                                     | 1.26 sec: 1.35x slower                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 618 ms: 1.39x slower                                       |
| async_tree_none_tg         | 336 ms                                                     | 471 ms: 1.40x slower                                       |
| Geometric mean             | (ref)                                                      | 1.02x slower                                               |

Benchmark hidden because not significant (11): pylint, pickle_list, djangocms, regex_v8, asyncio_tcp_ssl, pyflate, sqlglot_transpile, fannkuch, xml_etree_parse, bench_mp_pool, deepcopy_memo
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser, dask

# HPT report

- Reliability score: 75.04% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.95x