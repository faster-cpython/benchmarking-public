# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a2
- machine: linux-x86_64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 0.95x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 272 ms: 1.03x slower                                       |
| chameleon      | 6.85 ms                                                | 6.93 ms: 1.01x slower                                      |
| docutils       | 2.58 sec                                               | 2.69 sec: 1.04x slower                                     |
| html5lib       | 64.5 ms                                                | 66.3 ms: 1.03x slower                                      |
| tornado_http   | 91.5 ms                                                | 97.6 ms: 1.07x slower                                      |
| Geometric mean | (ref)                                                  | 1.03x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| coroutines                 | 22.5 ms                                                | 21.8 ms: 1.03x faster                                      |
| asyncio_websockets         | 555 ms                                                 | 563 ms: 1.01x slower                                       |
| asyncio_tcp                | 488 ms                                                 | 501 ms: 1.03x slower                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.84 sec: 1.03x slower                                     |
| async_generators           | 433 ms                                                 | 459 ms: 1.06x slower                                       |
| async_tree_none            | 354 ms                                                 | 451 ms: 1.27x slower                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 733 ms: 1.28x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 583 ms: 1.32x slower                                       |
| async_tree_memoization_tg  | 465 ms                                                 | 618 ms: 1.33x slower                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 760 ms: 1.40x slower                                       |
| async_tree_io              | 843 ms                                                 | 1.22 sec: 1.45x slower                                     |
| async_tree_none_tg         | 320 ms                                                 | 471 ms: 1.47x slower                                       |
| async_tree_io_tg           | 825 ms                                                 | 1.26 sec: 1.53x slower                                     |
| Geometric mean             | (ref)                                                  | 1.23x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 197 ms: 1.06x slower                                       |
| nbody          | 85.7 ms                                                | 91.0 ms: 1.06x slower                                      |
| float          | 78.5 ms                                                | 83.5 ms: 1.06x slower                                      |
| Geometric mean | (ref)                                                  | 1.06x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.57 ms: 1.09x faster                                      |
| regex_v8       | 25.3 ms                                                | 25.0 ms: 1.01x faster                                      |
| regex_compile  | 131 ms                                                 | 137 ms: 1.05x slower                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                               |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 88.2 ms: 1.01x slower                                      |
| pickle               | 11.6 us                                                | 11.8 us: 1.02x slower                                      |
| json_dumps           | 10.4 ms                                                | 10.7 ms: 1.02x slower                                      |
| unpickle_list        | 4.96 us                                                | 5.12 us: 1.03x slower                                      |
| xml_etree_parse      | 156 ms                                                 | 162 ms: 1.04x slower                                       |
| pickle_pure_python   | 300 us                                                 | 313 us: 1.04x slower                                       |
| unpickle_pure_python | 213 us                                                 | 224 us: 1.05x slower                                       |
| pickle_dict          | 33.2 us                                                | 34.9 us: 1.05x slower                                      |
| tomli_loads          | 2.11 sec                                               | 2.23 sec: 1.05x slower                                     |
| unpickle             | 14.9 us                                                | 15.7 us: 1.06x slower                                      |
| xml_etree_iterparse  | 102 ms                                                 | 108 ms: 1.06x slower                                       |
| json_loads           | 27.0 us                                                | 28.7 us: 1.06x slower                                      |
| Geometric mean       | (ref)                                                  | 1.04x slower                                               |

Benchmark hidden because not significant (2): xml_etree_process, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.7 ms: 1.01x slower                                      |
| python_startup_no_site | 6.99 ms                                                | 9.26 ms: 1.33x slower                                      |
| Geometric mean         | (ref)                                                  | 1.16x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| django_template | 34.4 ms                                                | 35.2 ms: 1.02x slower                                      |
| genshi_xml      | 50.3 ms                                                | 52.1 ms: 1.03x slower                                      |
| genshi_text     | 22.9 ms                                                | 23.8 ms: 1.04x slower                                      |
| mako            | 11.1 ms                                                | 11.7 ms: 1.05x slower                                      |
| Geometric mean  | (ref)                                                  | 1.04x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols   | 159 us                                                 | 119 us: 1.34x faster                                       |
| mypy2                      | 1.07 sec                                               | 866 ms: 1.23x faster                                       |
| regex_effbot               | 3.88 ms                                                | 3.57 ms: 1.09x faster                                      |
| create_gc_cycles           | 1.61 ms                                                | 1.48 ms: 1.08x faster                                      |
| flaskblogging              | 9.11 ms                                                | 8.70 ms: 1.05x faster                                      |
| mdp                        | 2.74 sec                                               | 2.64 sec: 1.04x faster                                     |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.04x faster                                       |
| coroutines                 | 22.5 ms                                                | 21.8 ms: 1.03x faster                                      |
| djangocms                  | 31.9 us                                                | 31.4 us: 1.02x faster                                      |
| regex_v8                   | 25.3 ms                                                | 25.0 ms: 1.01x faster                                      |
| deepcopy_reduce            | 3.17 us                                                | 3.14 us: 1.01x faster                                      |
| sqlglot_normalize          | 107 ms                                                 | 107 ms: 1.00x faster                                       |
| deepcopy                   | 352 us                                                 | 354 us: 1.00x slower                                       |
| crypto_pyaes               | 73.0 ms                                                | 73.3 ms: 1.01x slower                                      |
| sympy_integrate            | 19.9 ms                                                | 20.0 ms: 1.01x slower                                      |
| sqlglot_optimize           | 53.9 ms                                                | 54.3 ms: 1.01x slower                                      |
| sqlite_synth               | 2.85 us                                                | 2.87 us: 1.01x slower                                      |
| json                       | 5.20 ms                                                | 5.24 ms: 1.01x slower                                      |
| python_startup             | 10.6 ms                                                | 10.7 ms: 1.01x slower                                      |
| thrift                     | 796 us                                                 | 805 us: 1.01x slower                                       |
| pprint_safe_repr           | 744 ms                                                 | 753 ms: 1.01x slower                                       |
| chameleon                  | 6.85 ms                                                | 6.93 ms: 1.01x slower                                      |
| richards_super             | 54.4 ms                                                | 55.1 ms: 1.01x slower                                      |
| sympy_sum                  | 150 ms                                                 | 151 ms: 1.01x slower                                       |
| asyncio_websockets         | 555 ms                                                 | 563 ms: 1.01x slower                                       |
| scimark_lu                 | 115 ms                                                 | 117 ms: 1.01x slower                                       |
| xml_etree_generate         | 87.0 ms                                                | 88.2 ms: 1.01x slower                                      |
| pprint_pformat             | 1.51 sec                                               | 1.54 sec: 1.02x slower                                     |
| scimark_fft                | 369 ms                                                 | 375 ms: 1.02x slower                                       |
| pickle                     | 11.6 us                                                | 11.8 us: 1.02x slower                                      |
| aiohttp                    | 1.14 ms                                                | 1.17 ms: 1.02x slower                                      |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.13 ms: 1.02x slower                                      |
| json_dumps                 | 10.4 ms                                                | 10.7 ms: 1.02x slower                                      |
| django_template            | 34.4 ms                                                | 35.2 ms: 1.02x slower                                      |
| 2to3                       | 265 ms                                                 | 272 ms: 1.03x slower                                       |
| meteor_contest             | 108 ms                                                 | 110 ms: 1.03x slower                                       |
| asyncio_tcp                | 488 ms                                                 | 501 ms: 1.03x slower                                       |
| html5lib                   | 64.5 ms                                                | 66.3 ms: 1.03x slower                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.84 sec: 1.03x slower                                     |
| unpickle_list              | 4.96 us                                                | 5.12 us: 1.03x slower                                      |
| hexiom                     | 6.13 ms                                                | 6.32 ms: 1.03x slower                                      |
| scimark_sor                | 122 ms                                                 | 126 ms: 1.03x slower                                       |
| richards                   | 48.1 ms                                                | 49.7 ms: 1.03x slower                                      |
| gunicorn                   | 1.23 ms                                                | 1.27 ms: 1.03x slower                                      |
| genshi_xml                 | 50.3 ms                                                | 52.1 ms: 1.03x slower                                      |
| nqueens                    | 80.6 ms                                                | 83.5 ms: 1.04x slower                                      |
| sqlglot_parse              | 1.27 ms                                                | 1.31 ms: 1.04x slower                                      |
| xml_etree_parse            | 156 ms                                                 | 162 ms: 1.04x slower                                       |
| sqlglot_transpile          | 1.57 ms                                                | 1.64 ms: 1.04x slower                                      |
| comprehensions             | 16.4 us                                                | 17.0 us: 1.04x slower                                      |
| logging_simple             | 5.66 us                                                | 5.89 us: 1.04x slower                                      |
| logging_format             | 6.25 us                                                | 6.50 us: 1.04x slower                                      |
| docutils                   | 2.58 sec                                               | 2.69 sec: 1.04x slower                                     |
| genshi_text                | 22.9 ms                                                | 23.8 ms: 1.04x slower                                      |
| pickle_pure_python         | 300 us                                                 | 313 us: 1.04x slower                                       |
| go                         | 142 ms                                                 | 148 ms: 1.04x slower                                       |
| generators                 | 28.8 ms                                                | 30.1 ms: 1.05x slower                                      |
| regex_compile              | 131 ms                                                 | 137 ms: 1.05x slower                                       |
| bench_thread_pool          | 815 us                                                 | 852 us: 1.05x slower                                       |
| deepcopy_memo              | 38.0 us                                                | 39.8 us: 1.05x slower                                      |
| unpickle_pure_python       | 213 us                                                 | 224 us: 1.05x slower                                       |
| mako                       | 11.1 ms                                                | 11.7 ms: 1.05x slower                                      |
| pickle_dict                | 33.2 us                                                | 34.9 us: 1.05x slower                                      |
| tomli_loads                | 2.11 sec                                               | 2.23 sec: 1.05x slower                                     |
| pyflate                    | 460 ms                                                 | 484 ms: 1.05x slower                                       |
| unpickle                   | 14.9 us                                                | 15.7 us: 1.06x slower                                      |
| scimark_monte_carlo        | 66.3 ms                                                | 70.0 ms: 1.06x slower                                      |
| fannkuch                   | 381 ms                                                 | 402 ms: 1.06x slower                                       |
| async_generators           | 433 ms                                                 | 459 ms: 1.06x slower                                       |
| pidigits                   | 186 ms                                                 | 197 ms: 1.06x slower                                       |
| xml_etree_iterparse        | 102 ms                                                 | 108 ms: 1.06x slower                                       |
| nbody                      | 85.7 ms                                                | 91.0 ms: 1.06x slower                                      |
| json_loads                 | 27.0 us                                                | 28.7 us: 1.06x slower                                      |
| float                      | 78.5 ms                                                | 83.5 ms: 1.06x slower                                      |
| logging_silent             | 102 ns                                                 | 109 ns: 1.07x slower                                       |
| tornado_http               | 91.5 ms                                                | 97.6 ms: 1.07x slower                                      |
| dulwich_log                | 63.0 ms                                                | 67.6 ms: 1.07x slower                                      |
| chaos                      | 58.4 ms                                                | 63.4 ms: 1.09x slower                                      |
| raytrace                   | 262 ms                                                 | 284 ms: 1.09x slower                                       |
| pathlib                    | 17.1 ms                                                | 18.6 ms: 1.09x slower                                      |
| deltablue                  | 3.15 ms                                                | 3.44 ms: 1.09x slower                                      |
| coverage                   | 83.7 ms                                                | 95.2 ms: 1.14x slower                                      |
| gc_traversal               | 3.81 ms                                                | 4.37 ms: 1.15x slower                                      |
| async_tree_none            | 354 ms                                                 | 451 ms: 1.27x slower                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 733 ms: 1.28x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 583 ms: 1.32x slower                                       |
| python_startup_no_site     | 6.99 ms                                                | 9.26 ms: 1.33x slower                                      |
| async_tree_memoization_tg  | 465 ms                                                 | 618 ms: 1.33x slower                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 760 ms: 1.40x slower                                       |
| async_tree_io              | 843 ms                                                 | 1.22 sec: 1.45x slower                                     |
| async_tree_none_tg         | 320 ms                                                 | 471 ms: 1.47x slower                                       |
| async_tree_io_tg           | 825 ms                                                 | 1.26 sec: 1.53x slower                                     |
| Geometric mean             | (ref)                                                  | 1.05x slower                                               |

Benchmark hidden because not significant (9): sympy_expand, pycparser, bench_mp_pool, sympy_str, regex_dna, pylint, xml_etree_process, telco, pickle_list
Ignored benchmarks (3) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, dask, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 0.95x