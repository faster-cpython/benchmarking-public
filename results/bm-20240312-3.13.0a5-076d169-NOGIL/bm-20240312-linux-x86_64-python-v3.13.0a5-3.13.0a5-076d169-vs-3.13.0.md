# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a5
- machine: linux-x86_64
- commit hash: 076d169
- commit date: 2024-03-12
- overall geometric mean: 1.47x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 377 ms: 1.42x slower                                       |
| chameleon      | 6.85 ms                                                | 12.3 ms: 1.79x slower                                      |
| docutils       | 2.58 sec                                               | 3.28 sec: 1.27x slower                                     |
| html5lib       | 64.5 ms                                                | 91.5 ms: 1.42x slower                                      |
| tornado_http   | 91.5 ms                                                | 137 ms: 1.50x slower                                       |
| Geometric mean | (ref)                                                  | 1.47x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 472 ms: 1.02x slower                                       |
| async_tree_io_tg           | 825 ms                                                 | 839 ms: 1.02x slower                                       |
| asyncio_websockets         | 555 ms                                                 | 567 ms: 1.02x slower                                       |
| async_tree_io              | 843 ms                                                 | 877 ms: 1.04x slower                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.99 sec: 1.11x slower                                     |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 623 ms: 1.15x slower                                       |
| async_tree_none_tg         | 320 ms                                                 | 369 ms: 1.15x slower                                       |
| async_tree_none            | 354 ms                                                 | 412 ms: 1.16x slower                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 668 ms: 1.16x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 518 ms: 1.17x slower                                       |
| async_generators           | 433 ms                                                 | 511 ms: 1.18x slower                                       |
| asyncio_tcp                | 488 ms                                                 | 584 ms: 1.20x slower                                       |
| coroutines                 | 22.5 ms                                                | 29.3 ms: 1.30x slower                                      |
| Geometric mean             | (ref)                                                  | 1.13x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 192 ms: 1.03x slower                                       |
| float          | 78.5 ms                                                | 127 ms: 1.61x slower                                       |
| nbody          | 85.7 ms                                                | 215 ms: 2.50x slower                                       |
| Geometric mean | (ref)                                                  | 1.61x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.56 ms: 1.09x faster                                      |
| regex_dna      | 220 ms                                                 | 230 ms: 1.04x slower                                       |
| regex_v8       | 25.3 ms                                                | 26.9 ms: 1.07x slower                                      |
| regex_compile  | 131 ms                                                 | 204 ms: 1.56x slower                                       |
| Geometric mean | (ref)                                                  | 1.12x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_list          | 5.01 us                                                | 4.97 us: 1.01x faster                                      |
| pickle               | 11.6 us                                                | 12.1 us: 1.04x slower                                      |
| xml_etree_iterparse  | 102 ms                                                 | 117 ms: 1.15x slower                                       |
| unpickle_list        | 4.96 us                                                | 5.75 us: 1.16x slower                                      |
| unpickle             | 14.9 us                                                | 18.1 us: 1.22x slower                                      |
| xml_etree_generate   | 87.0 ms                                                | 108 ms: 1.24x slower                                       |
| pickle_dict          | 33.2 us                                                | 41.4 us: 1.25x slower                                      |
| json_loads           | 27.0 us                                                | 34.8 us: 1.29x slower                                      |
| json_dumps           | 10.4 ms                                                | 13.7 ms: 1.32x slower                                      |
| xml_etree_process    | 60.4 ms                                                | 86.4 ms: 1.43x slower                                      |
| tomli_loads          | 2.11 sec                                               | 3.11 sec: 1.47x slower                                     |
| unpickle_pure_python | 213 us                                                 | 367 us: 1.72x slower                                       |
| pickle_pure_python   | 300 us                                                 | 528 us: 1.76x slower                                       |
| Geometric mean       | (ref)                                                  | 1.27x slower                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 13.6 ms: 1.29x slower                                      |
| python_startup_no_site | 6.99 ms                                                | 11.6 ms: 1.66x slower                                      |
| Geometric mean         | (ref)                                                  | 1.46x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_xml      | 50.3 ms                                                | 78.4 ms: 1.56x slower                                      |
| django_template | 34.4 ms                                                | 57.7 ms: 1.68x slower                                      |
| genshi_text     | 22.9 ms                                                | 38.9 ms: 1.70x slower                                      |
| mako            | 11.1 ms                                                | 21.0 ms: 1.89x slower                                      |
| Geometric mean  | (ref)                                                  | 1.70x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| create_gc_cycles           | 1.61 ms                                                | 1.08 ms: 1.49x faster                                      |
| gc_traversal               | 3.81 ms                                                | 2.57 ms: 1.48x faster                                      |
| regex_effbot               | 3.88 ms                                                | 3.56 ms: 1.09x faster                                      |
| pickle_list                | 5.01 us                                                | 4.97 us: 1.01x faster                                      |
| bench_mp_pool              | 24.0 ms                                                | 23.9 ms: 1.01x faster                                      |
| async_tree_memoization_tg  | 465 ms                                                 | 472 ms: 1.02x slower                                       |
| async_tree_io_tg           | 825 ms                                                 | 839 ms: 1.02x slower                                       |
| asyncio_websockets         | 555 ms                                                 | 567 ms: 1.02x slower                                       |
| pidigits                   | 186 ms                                                 | 192 ms: 1.03x slower                                       |
| async_tree_io              | 843 ms                                                 | 877 ms: 1.04x slower                                       |
| pickle                     | 11.6 us                                                | 12.1 us: 1.04x slower                                      |
| regex_dna                  | 220 ms                                                 | 230 ms: 1.04x slower                                       |
| typing_runtime_protocols   | 159 us                                                 | 167 us: 1.05x slower                                       |
| regex_v8                   | 25.3 ms                                                | 26.9 ms: 1.07x slower                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.99 sec: 1.11x slower                                     |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 623 ms: 1.15x slower                                       |
| xml_etree_iterparse        | 102 ms                                                 | 117 ms: 1.15x slower                                       |
| async_tree_none_tg         | 320 ms                                                 | 369 ms: 1.15x slower                                       |
| unpickle_list              | 4.96 us                                                | 5.75 us: 1.16x slower                                      |
| async_tree_none            | 354 ms                                                 | 412 ms: 1.16x slower                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 668 ms: 1.16x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 518 ms: 1.17x slower                                       |
| async_generators           | 433 ms                                                 | 511 ms: 1.18x slower                                       |
| asyncio_tcp                | 488 ms                                                 | 584 ms: 1.20x slower                                       |
| json                       | 5.20 ms                                                | 6.24 ms: 1.20x slower                                      |
| mdp                        | 2.74 sec                                               | 3.30 sec: 1.20x slower                                     |
| unpickle                   | 14.9 us                                                | 18.1 us: 1.22x slower                                      |
| xml_etree_generate         | 87.0 ms                                                | 108 ms: 1.24x slower                                       |
| pylint                     | 313 ms                                                 | 390 ms: 1.25x slower                                       |
| pickle_dict                | 33.2 us                                                | 41.4 us: 1.25x slower                                      |
| generators                 | 28.8 ms                                                | 36.2 ms: 1.26x slower                                      |
| meteor_contest             | 108 ms                                                 | 136 ms: 1.26x slower                                       |
| docutils                   | 2.58 sec                                               | 3.28 sec: 1.27x slower                                     |
| json_loads                 | 27.0 us                                                | 34.8 us: 1.29x slower                                      |
| python_startup             | 10.6 ms                                                | 13.6 ms: 1.29x slower                                      |
| coroutines                 | 22.5 ms                                                | 29.3 ms: 1.30x slower                                      |
| scimark_fft                | 369 ms                                                 | 481 ms: 1.30x slower                                       |
| json_dumps                 | 10.4 ms                                                | 13.7 ms: 1.32x slower                                      |
| pycparser                  | 1.19 sec                                               | 1.57 sec: 1.32x slower                                     |
| sqlite_synth               | 2.85 us                                                | 3.84 us: 1.35x slower                                      |
| nqueens                    | 80.6 ms                                                | 111 ms: 1.38x slower                                       |
| telco                      | 8.45 ms                                                | 11.7 ms: 1.38x slower                                      |
| aiohttp                    | 1.14 ms                                                | 1.59 ms: 1.39x slower                                      |
| gunicorn                   | 1.23 ms                                                | 1.71 ms: 1.39x slower                                      |
| richards                   | 48.1 ms                                                | 68.0 ms: 1.41x slower                                      |
| dulwich_log                | 63.0 ms                                                | 89.2 ms: 1.42x slower                                      |
| html5lib                   | 64.5 ms                                                | 91.5 ms: 1.42x slower                                      |
| 2to3                       | 265 ms                                                 | 377 ms: 1.42x slower                                       |
| sympy_integrate            | 19.9 ms                                                | 28.4 ms: 1.43x slower                                      |
| xml_etree_process          | 60.4 ms                                                | 86.4 ms: 1.43x slower                                      |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 7.26 ms: 1.44x slower                                      |
| fannkuch                   | 381 ms                                                 | 559 ms: 1.47x slower                                       |
| tomli_loads                | 2.11 sec                                               | 3.11 sec: 1.47x slower                                     |
| crypto_pyaes               | 73.0 ms                                                | 108 ms: 1.48x slower                                       |
| deepcopy                   | 352 us                                                 | 527 us: 1.49x slower                                       |
| deepcopy_reduce            | 3.17 us                                                | 4.74 us: 1.50x slower                                      |
| tornado_http               | 91.5 ms                                                | 137 ms: 1.50x slower                                       |
| richards_super             | 54.4 ms                                                | 82.3 ms: 1.51x slower                                      |
| pathlib                    | 17.1 ms                                                | 25.9 ms: 1.52x slower                                      |
| sympy_str                  | 274 ms                                                 | 421 ms: 1.54x slower                                       |
| genshi_xml                 | 50.3 ms                                                | 78.4 ms: 1.56x slower                                      |
| regex_compile              | 131 ms                                                 | 204 ms: 1.56x slower                                       |
| comprehensions             | 16.4 us                                                | 25.7 us: 1.56x slower                                      |
| spectral_norm              | 115 ms                                                 | 181 ms: 1.57x slower                                       |
| flaskblogging              | 9.11 ms                                                | 14.3 ms: 1.57x slower                                      |
| pyflate                    | 460 ms                                                 | 728 ms: 1.58x slower                                       |
| deepcopy_memo              | 38.0 us                                                | 60.8 us: 1.60x slower                                      |
| sympy_expand               | 462 ms                                                 | 740 ms: 1.60x slower                                       |
| float                      | 78.5 ms                                                | 127 ms: 1.61x slower                                       |
| pprint_safe_repr           | 744 ms                                                 | 1.20 sec: 1.61x slower                                     |
| sqlglot_optimize           | 53.9 ms                                                | 88.8 ms: 1.65x slower                                      |
| pprint_pformat             | 1.51 sec                                               | 2.49 sec: 1.65x slower                                     |
| sqlglot_normalize          | 107 ms                                                 | 177 ms: 1.65x slower                                       |
| python_startup_no_site     | 6.99 ms                                                | 11.6 ms: 1.66x slower                                      |
| django_template            | 34.4 ms                                                | 57.7 ms: 1.68x slower                                      |
| sympy_sum                  | 150 ms                                                 | 254 ms: 1.70x slower                                       |
| genshi_text                | 22.9 ms                                                | 38.9 ms: 1.70x slower                                      |
| unpickle_pure_python       | 213 us                                                 | 367 us: 1.72x slower                                       |
| logging_silent             | 102 ns                                                 | 176 ns: 1.72x slower                                       |
| pickle_pure_python         | 300 us                                                 | 528 us: 1.76x slower                                       |
| chameleon                  | 6.85 ms                                                | 12.3 ms: 1.79x slower                                      |
| logging_simple             | 5.66 us                                                | 10.2 us: 1.79x slower                                      |
| logging_format             | 6.25 us                                                | 11.2 us: 1.79x slower                                      |
| scimark_monte_carlo        | 66.3 ms                                                | 119 ms: 1.80x slower                                       |
| hexiom                     | 6.13 ms                                                | 11.0 ms: 1.80x slower                                      |
| sqlglot_transpile          | 1.57 ms                                                | 2.84 ms: 1.81x slower                                      |
| sqlglot_parse              | 1.27 ms                                                | 2.37 ms: 1.87x slower                                      |
| mako                       | 11.1 ms                                                | 21.0 ms: 1.89x slower                                      |
| go                         | 142 ms                                                 | 273 ms: 1.93x slower                                       |
| scimark_sor                | 122 ms                                                 | 241 ms: 1.97x slower                                       |
| chaos                      | 58.4 ms                                                | 115 ms: 1.97x slower                                       |
| raytrace                   | 262 ms                                                 | 518 ms: 1.98x slower                                       |
| scimark_lu                 | 115 ms                                                 | 250 ms: 2.18x slower                                       |
| deltablue                  | 3.15 ms                                                | 7.43 ms: 2.36x slower                                      |
| nbody                      | 85.7 ms                                                | 215 ms: 2.50x slower                                       |
| bench_thread_pool          | 815 us                                                 | 3.01 ms: 3.69x slower                                      |
| coverage                   | 83.7 ms                                                | 891 ms: 10.64x slower                                      |
| thrift                     | 796 us                                                 | 12.4 ms: 15.55x slower                                     |
| Geometric mean             | (ref)                                                  | 1.47x slower                                               |

Benchmark hidden because not significant (2): xml_etree_parse, mypy2
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, dask, djangocms, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.37x
- 95% likely to have a slowdown of 1.34x
- 99% likely to have a slowdown of 1.31x

# Memory
- memory change: 1.10x