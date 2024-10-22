# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a5
- machine: linux-x86_64
- commit hash: 076d169
- commit date: 2024-03-12
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 270 ms: 1.02x slower                                       |
| docutils       | 2.58 sec                                               | 2.66 sec: 1.03x slower                                     |
| html5lib       | 64.5 ms                                                | 67.4 ms: 1.04x slower                                      |
| tornado_http   | 91.5 ms                                                | 98.6 ms: 1.08x slower                                      |
| Geometric mean | (ref)                                                  | 1.03x slower                                               |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| coroutines                 | 22.5 ms                                                | 22.0 ms: 1.02x faster                                      |
| asyncio_websockets         | 555 ms                                                 | 563 ms: 1.01x slower                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.85 sec: 1.03x slower                                     |
| asyncio_tcp                | 488 ms                                                 | 504 ms: 1.03x slower                                       |
| async_generators           | 433 ms                                                 | 449 ms: 1.04x slower                                       |
| async_tree_none            | 354 ms                                                 | 449 ms: 1.27x slower                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 729 ms: 1.27x slower                                       |
| async_tree_memoization_tg  | 465 ms                                                 | 595 ms: 1.28x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 581 ms: 1.31x slower                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 745 ms: 1.37x slower                                       |
| async_tree_io              | 843 ms                                                 | 1.22 sec: 1.44x slower                                     |
| async_tree_none_tg         | 320 ms                                                 | 463 ms: 1.45x slower                                       |
| async_tree_io_tg           | 825 ms                                                 | 1.24 sec: 1.50x slower                                     |
| Geometric mean             | (ref)                                                  | 1.22x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 189 ms: 1.02x slower                                       |
| float          | 78.5 ms                                                | 82.6 ms: 1.05x slower                                      |
| nbody          | 85.7 ms                                                | 93.6 ms: 1.09x slower                                      |
| Geometric mean | (ref)                                                  | 1.05x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.54 ms: 1.10x faster                                      |
| regex_v8       | 25.3 ms                                                | 24.7 ms: 1.02x faster                                      |
| regex_dna      | 220 ms                                                 | 216 ms: 1.02x faster                                       |
| regex_compile  | 131 ms                                                 | 133 ms: 1.01x slower                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| xml_etree_process    | 60.4 ms                                                | 59.8 ms: 1.01x faster                                      |
| xml_etree_generate   | 87.0 ms                                                | 87.3 ms: 1.00x slower                                      |
| pickle_pure_python   | 300 us                                                 | 302 us: 1.01x slower                                       |
| pickle               | 11.6 us                                                | 11.7 us: 1.01x slower                                      |
| unpickle             | 14.9 us                                                | 15.1 us: 1.01x slower                                      |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                       |
| unpickle_list        | 4.96 us                                                | 5.05 us: 1.02x slower                                      |
| xml_etree_parse      | 156 ms                                                 | 159 ms: 1.02x slower                                       |
| tomli_loads          | 2.11 sec                                               | 2.16 sec: 1.02x slower                                     |
| json_loads           | 27.0 us                                                | 27.7 us: 1.03x slower                                      |
| json_dumps           | 10.4 ms                                                | 10.8 ms: 1.04x slower                                      |
| xml_etree_iterparse  | 102 ms                                                 | 106 ms: 1.04x slower                                       |
| pickle_dict          | 33.2 us                                                | 35.7 us: 1.08x slower                                      |
| Geometric mean       | (ref)                                                  | 1.02x slower                                               |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.4 ms: 1.01x faster                                      |
| python_startup_no_site | 6.99 ms                                                | 8.99 ms: 1.29x slower                                      |
| Geometric mean         | (ref)                                                  | 1.13x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| django_template | 34.4 ms                                                | 33.8 ms: 1.02x faster                                      |
| mako            | 11.1 ms                                                | 11.3 ms: 1.02x slower                                      |
| genshi_xml      | 50.3 ms                                                | 52.0 ms: 1.03x slower                                      |
| Geometric mean  | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols   | 159 us                                                 | 112 us: 1.42x faster                                       |
| mypy2                      | 1.07 sec                                               | 871 ms: 1.23x faster                                       |
| regex_effbot               | 3.88 ms                                                | 3.54 ms: 1.10x faster                                      |
| mdp                        | 2.74 sec                                               | 2.53 sec: 1.08x faster                                     |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.68 ms: 1.07x faster                                      |
| spectral_norm              | 115 ms                                                 | 108 ms: 1.07x faster                                       |
| create_gc_cycles           | 1.61 ms                                                | 1.52 ms: 1.06x faster                                      |
| richards                   | 48.1 ms                                                | 45.9 ms: 1.05x faster                                      |
| richards_super             | 54.4 ms                                                | 51.9 ms: 1.05x faster                                      |
| deepcopy_reduce            | 3.17 us                                                | 3.04 us: 1.04x faster                                      |
| flaskblogging              | 9.11 ms                                                | 8.82 ms: 1.03x faster                                      |
| logging_silent             | 102 ns                                                 | 99.5 ns: 1.03x faster                                      |
| regex_v8                   | 25.3 ms                                                | 24.7 ms: 1.02x faster                                      |
| coroutines                 | 22.5 ms                                                | 22.0 ms: 1.02x faster                                      |
| go                         | 142 ms                                                 | 139 ms: 1.02x faster                                       |
| regex_dna                  | 220 ms                                                 | 216 ms: 1.02x faster                                       |
| django_template            | 34.4 ms                                                | 33.8 ms: 1.02x faster                                      |
| scimark_fft                | 369 ms                                                 | 362 ms: 1.02x faster                                       |
| deepcopy                   | 352 us                                                 | 346 us: 1.02x faster                                       |
| scimark_lu                 | 115 ms                                                 | 113 ms: 1.02x faster                                       |
| python_startup             | 10.6 ms                                                | 10.4 ms: 1.01x faster                                      |
| json                       | 5.20 ms                                                | 5.15 ms: 1.01x faster                                      |
| xml_etree_process          | 60.4 ms                                                | 59.8 ms: 1.01x faster                                      |
| pycparser                  | 1.19 sec                                               | 1.18 sec: 1.01x faster                                     |
| thrift                     | 796 us                                                 | 790 us: 1.01x faster                                       |
| gc_traversal               | 3.81 ms                                                | 3.78 ms: 1.01x faster                                      |
| sqlglot_normalize          | 107 ms                                                 | 107 ms: 1.01x faster                                       |
| bench_mp_pool              | 24.0 ms                                                | 23.9 ms: 1.01x faster                                      |
| hexiom                     | 6.13 ms                                                | 6.13 ms: 1.00x slower                                      |
| xml_etree_generate         | 87.0 ms                                                | 87.3 ms: 1.00x slower                                      |
| scimark_sor                | 122 ms                                                 | 123 ms: 1.00x slower                                       |
| sqlglot_parse              | 1.27 ms                                                | 1.27 ms: 1.00x slower                                      |
| raytrace                   | 262 ms                                                 | 263 ms: 1.01x slower                                       |
| sympy_integrate            | 19.9 ms                                                | 20.0 ms: 1.01x slower                                      |
| pickle_pure_python         | 300 us                                                 | 302 us: 1.01x slower                                       |
| pickle                     | 11.6 us                                                | 11.7 us: 1.01x slower                                      |
| sqlite_synth               | 2.85 us                                                | 2.89 us: 1.01x slower                                      |
| sqlglot_transpile          | 1.57 ms                                                | 1.59 ms: 1.01x slower                                      |
| regex_compile              | 131 ms                                                 | 133 ms: 1.01x slower                                       |
| meteor_contest             | 108 ms                                                 | 109 ms: 1.01x slower                                       |
| unpickle                   | 14.9 us                                                | 15.1 us: 1.01x slower                                      |
| asyncio_websockets         | 555 ms                                                 | 563 ms: 1.01x slower                                       |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                       |
| pprint_safe_repr           | 744 ms                                                 | 757 ms: 1.02x slower                                       |
| pidigits                   | 186 ms                                                 | 189 ms: 1.02x slower                                       |
| unpickle_list              | 4.96 us                                                | 5.05 us: 1.02x slower                                      |
| telco                      | 8.45 ms                                                | 8.60 ms: 1.02x slower                                      |
| 2to3                       | 265 ms                                                 | 270 ms: 1.02x slower                                       |
| mako                       | 11.1 ms                                                | 11.3 ms: 1.02x slower                                      |
| pyflate                    | 460 ms                                                 | 469 ms: 1.02x slower                                       |
| xml_etree_parse            | 156 ms                                                 | 159 ms: 1.02x slower                                       |
| tomli_loads                | 2.11 sec                                               | 2.16 sec: 1.02x slower                                     |
| sympy_sum                  | 150 ms                                                 | 153 ms: 1.02x slower                                       |
| deltablue                  | 3.15 ms                                                | 3.23 ms: 1.03x slower                                      |
| scimark_monte_carlo        | 66.3 ms                                                | 67.9 ms: 1.03x slower                                      |
| generators                 | 28.8 ms                                                | 29.5 ms: 1.03x slower                                      |
| json_loads                 | 27.0 us                                                | 27.7 us: 1.03x slower                                      |
| pprint_pformat             | 1.51 sec                                               | 1.55 sec: 1.03x slower                                     |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.85 sec: 1.03x slower                                     |
| docutils                   | 2.58 sec                                               | 2.66 sec: 1.03x slower                                     |
| genshi_xml                 | 50.3 ms                                                | 52.0 ms: 1.03x slower                                      |
| asyncio_tcp                | 488 ms                                                 | 504 ms: 1.03x slower                                       |
| bench_thread_pool          | 815 us                                                 | 842 us: 1.03x slower                                       |
| logging_simple             | 5.66 us                                                | 5.85 us: 1.03x slower                                      |
| json_dumps                 | 10.4 ms                                                | 10.8 ms: 1.04x slower                                      |
| async_generators           | 433 ms                                                 | 449 ms: 1.04x slower                                       |
| aiohttp                    | 1.14 ms                                                | 1.19 ms: 1.04x slower                                      |
| xml_etree_iterparse        | 102 ms                                                 | 106 ms: 1.04x slower                                       |
| chaos                      | 58.4 ms                                                | 60.9 ms: 1.04x slower                                      |
| logging_format             | 6.25 us                                                | 6.53 us: 1.04x slower                                      |
| html5lib                   | 64.5 ms                                                | 67.4 ms: 1.04x slower                                      |
| gunicorn                   | 1.23 ms                                                | 1.29 ms: 1.05x slower                                      |
| fannkuch                   | 381 ms                                                 | 400 ms: 1.05x slower                                       |
| float                      | 78.5 ms                                                | 82.6 ms: 1.05x slower                                      |
| dulwich_log                | 63.0 ms                                                | 67.3 ms: 1.07x slower                                      |
| pickle_dict                | 33.2 us                                                | 35.7 us: 1.08x slower                                      |
| tornado_http               | 91.5 ms                                                | 98.6 ms: 1.08x slower                                      |
| pathlib                    | 17.1 ms                                                | 18.5 ms: 1.09x slower                                      |
| nbody                      | 85.7 ms                                                | 93.6 ms: 1.09x slower                                      |
| dask                       | 338 ms                                                 | 370 ms: 1.09x slower                                       |
| coverage                   | 83.7 ms                                                | 95.6 ms: 1.14x slower                                      |
| async_tree_none            | 354 ms                                                 | 449 ms: 1.27x slower                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 729 ms: 1.27x slower                                       |
| async_tree_memoization_tg  | 465 ms                                                 | 595 ms: 1.28x slower                                       |
| python_startup_no_site     | 6.99 ms                                                | 8.99 ms: 1.29x slower                                      |
| async_tree_memoization     | 442 ms                                                 | 581 ms: 1.31x slower                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 745 ms: 1.37x slower                                       |
| async_tree_io              | 843 ms                                                 | 1.22 sec: 1.44x slower                                     |
| async_tree_none_tg         | 320 ms                                                 | 463 ms: 1.45x slower                                       |
| async_tree_io_tg           | 825 ms                                                 | 1.24 sec: 1.50x slower                                     |
| Geometric mean             | (ref)                                                  | 1.03x slower                                               |

Benchmark hidden because not significant (12): pylint, chameleon, sqlglot_optimize, comprehensions, crypto_pyaes, nqueens, pickle_list, deepcopy_memo, genshi_text, sympy_str, djangocms, sympy_expand
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 0.97x