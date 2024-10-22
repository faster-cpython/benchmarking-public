# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b2
- machine: linux-x86_64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.03x slower
- HPT reliability: 99.73%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 281 ms: 1.06x slower                                       |
| chameleon      | 6.85 ms                                                | 7.11 ms: 1.04x slower                                      |
| docutils       | 2.58 sec                                               | 2.99 sec: 1.16x slower                                     |
| html5lib       | 64.5 ms                                                | 69.1 ms: 1.07x slower                                      |
| tornado_http   | 91.5 ms                                                | 96.9 ms: 1.06x slower                                      |
| Geometric mean | (ref)                                                  | 1.08x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 441 ms: 1.05x faster                                       |
| asyncio_websockets         | 555 ms                                                 | 567 ms: 1.02x slower                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.86 sec: 1.04x slower                                     |
| async_tree_none_tg         | 320 ms                                                 | 333 ms: 1.04x slower                                       |
| async_tree_none            | 354 ms                                                 | 377 ms: 1.07x slower                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 612 ms: 1.07x slower                                       |
| async_generators           | 433 ms                                                 | 462 ms: 1.07x slower                                       |
| asyncio_tcp                | 488 ms                                                 | 522 ms: 1.07x slower                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 584 ms: 1.07x slower                                       |
| async_tree_io              | 843 ms                                                 | 932 ms: 1.11x slower                                       |
| async_tree_io_tg           | 825 ms                                                 | 945 ms: 1.15x slower                                       |
| Geometric mean             | (ref)                                                  | 1.05x slower                                               |

Benchmark hidden because not significant (2): coroutines, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 78.5 ms                                                | 73.0 ms: 1.07x faster                                      |
| nbody          | 85.7 ms                                                | 83.5 ms: 1.03x faster                                      |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.69 ms: 1.05x faster                                      |
| regex_dna      | 220 ms                                                 | 230 ms: 1.04x slower                                       |
| regex_compile  | 131 ms                                                 | 138 ms: 1.05x slower                                       |
| Geometric mean | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 1.95 sec: 1.08x faster                                     |
| xml_etree_generate   | 87.0 ms                                                | 82.9 ms: 1.05x faster                                      |
| xml_etree_parse      | 156 ms                                                 | 149 ms: 1.05x faster                                       |
| xml_etree_process    | 60.4 ms                                                | 58.5 ms: 1.03x faster                                      |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                      |
| pickle_list          | 5.01 us                                                | 5.08 us: 1.02x slower                                      |
| unpickle             | 14.9 us                                                | 15.1 us: 1.02x slower                                      |
| pickle               | 11.6 us                                                | 11.9 us: 1.03x slower                                      |
| unpickle_pure_python | 213 us                                                 | 222 us: 1.04x slower                                       |
| pickle_dict          | 33.2 us                                                | 34.8 us: 1.05x slower                                      |
| unpickle_list        | 4.96 us                                                | 5.26 us: 1.06x slower                                      |
| json_loads           | 27.0 us                                                | 28.8 us: 1.07x slower                                      |
| Geometric mean       | (ref)                                                  | 1.00x slower                                               |

Benchmark hidden because not significant (2): xml_etree_iterparse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 11.3 ms: 1.07x slower                                      |
| python_startup_no_site | 6.99 ms                                                | 7.62 ms: 1.09x slower                                      |
| Geometric mean         | (ref)                                                  | 1.08x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.83 ms: 1.13x faster                                      |
| django_template | 34.4 ms                                                | 36.4 ms: 1.06x slower                                      |
| genshi_text     | 22.9 ms                                                | 25.5 ms: 1.11x slower                                      |
| genshi_xml      | 50.3 ms                                                | 60.2 ms: 1.20x slower                                      |
| Geometric mean  | (ref)                                                  | 1.06x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mypy2                      | 1.07 sec                                               | 814 ms: 1.31x faster                                       |
| scimark_fft                | 369 ms                                                 | 317 ms: 1.16x faster                                       |
| richards                   | 48.1 ms                                                | 41.7 ms: 1.15x faster                                      |
| mako                       | 11.1 ms                                                | 9.83 ms: 1.13x faster                                      |
| richards_super             | 54.4 ms                                                | 48.4 ms: 1.13x faster                                      |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.13x faster                                       |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.48 ms: 1.12x faster                                      |
| tomli_loads                | 2.11 sec                                               | 1.95 sec: 1.08x faster                                     |
| float                      | 78.5 ms                                                | 73.0 ms: 1.07x faster                                      |
| crypto_pyaes               | 73.0 ms                                                | 68.0 ms: 1.07x faster                                      |
| fannkuch                   | 381 ms                                                 | 358 ms: 1.06x faster                                       |
| scimark_monte_carlo        | 66.3 ms                                                | 62.7 ms: 1.06x faster                                      |
| async_tree_memoization_tg  | 465 ms                                                 | 441 ms: 1.05x faster                                       |
| pyflate                    | 460 ms                                                 | 436 ms: 1.05x faster                                       |
| regex_effbot               | 3.88 ms                                                | 3.69 ms: 1.05x faster                                      |
| xml_etree_generate         | 87.0 ms                                                | 82.9 ms: 1.05x faster                                      |
| xml_etree_parse            | 156 ms                                                 | 149 ms: 1.05x faster                                       |
| mdp                        | 2.74 sec                                               | 2.62 sec: 1.05x faster                                     |
| pprint_safe_repr           | 744 ms                                                 | 715 ms: 1.04x faster                                       |
| telco                      | 8.45 ms                                                | 8.12 ms: 1.04x faster                                      |
| pprint_pformat             | 1.51 sec                                               | 1.45 sec: 1.04x faster                                     |
| xml_etree_process          | 60.4 ms                                                | 58.5 ms: 1.03x faster                                      |
| nbody                      | 85.7 ms                                                | 83.5 ms: 1.03x faster                                      |
| pycparser                  | 1.19 sec                                               | 1.17 sec: 1.02x faster                                     |
| deepcopy_memo              | 38.0 us                                                | 37.3 us: 1.02x faster                                      |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                      |
| logging_simple             | 5.66 us                                                | 5.70 us: 1.01x slower                                      |
| logging_format             | 6.25 us                                                | 6.30 us: 1.01x slower                                      |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                       |
| sqlite_synth               | 2.85 us                                                | 2.88 us: 1.01x slower                                      |
| pickle_list                | 5.01 us                                                | 5.08 us: 1.02x slower                                      |
| unpickle                   | 14.9 us                                                | 15.1 us: 1.02x slower                                      |
| flaskblogging              | 9.11 ms                                                | 9.27 ms: 1.02x slower                                      |
| gc_traversal               | 3.81 ms                                                | 3.88 ms: 1.02x slower                                      |
| comprehensions             | 16.4 us                                                | 16.7 us: 1.02x slower                                      |
| asyncio_websockets         | 555 ms                                                 | 567 ms: 1.02x slower                                       |
| pathlib                    | 17.1 ms                                                | 17.4 ms: 1.02x slower                                      |
| sqlglot_parse              | 1.27 ms                                                | 1.30 ms: 1.02x slower                                      |
| pickle                     | 11.6 us                                                | 11.9 us: 1.03x slower                                      |
| json                       | 5.20 ms                                                | 5.34 ms: 1.03x slower                                      |
| djangocms                  | 31.9 us                                                | 32.8 us: 1.03x slower                                      |
| meteor_contest             | 108 ms                                                 | 111 ms: 1.03x slower                                       |
| sqlglot_transpile          | 1.57 ms                                                | 1.63 ms: 1.03x slower                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.86 sec: 1.04x slower                                     |
| thrift                     | 796 us                                                 | 826 us: 1.04x slower                                       |
| chameleon                  | 6.85 ms                                                | 7.11 ms: 1.04x slower                                      |
| unpickle_pure_python       | 213 us                                                 | 222 us: 1.04x slower                                       |
| bpe_tokeniser              | 4.69 sec                                               | 4.88 sec: 1.04x slower                                     |
| async_tree_none_tg         | 320 ms                                                 | 333 ms: 1.04x slower                                       |
| deepcopy_reduce            | 3.17 us                                                | 3.30 us: 1.04x slower                                      |
| regex_dna                  | 220 ms                                                 | 230 ms: 1.04x slower                                       |
| scimark_sor                | 122 ms                                                 | 128 ms: 1.05x slower                                       |
| pickle_dict                | 33.2 us                                                | 34.8 us: 1.05x slower                                      |
| logging_silent             | 102 ns                                                 | 108 ns: 1.05x slower                                       |
| sqlglot_optimize           | 53.9 ms                                                | 56.8 ms: 1.05x slower                                      |
| regex_compile              | 131 ms                                                 | 138 ms: 1.05x slower                                       |
| django_template            | 34.4 ms                                                | 36.4 ms: 1.06x slower                                      |
| sqlglot_normalize          | 107 ms                                                 | 114 ms: 1.06x slower                                       |
| tornado_http               | 91.5 ms                                                | 96.9 ms: 1.06x slower                                      |
| 2to3                       | 265 ms                                                 | 281 ms: 1.06x slower                                       |
| unpickle_list              | 4.96 us                                                | 5.26 us: 1.06x slower                                      |
| deepcopy                   | 352 us                                                 | 375 us: 1.06x slower                                       |
| bench_thread_pool          | 815 us                                                 | 867 us: 1.06x slower                                       |
| async_tree_none            | 354 ms                                                 | 377 ms: 1.07x slower                                       |
| python_startup             | 10.6 ms                                                | 11.3 ms: 1.07x slower                                      |
| go                         | 142 ms                                                 | 151 ms: 1.07x slower                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 612 ms: 1.07x slower                                       |
| async_generators           | 433 ms                                                 | 462 ms: 1.07x slower                                       |
| json_loads                 | 27.0 us                                                | 28.8 us: 1.07x slower                                      |
| raytrace                   | 262 ms                                                 | 280 ms: 1.07x slower                                       |
| asyncio_tcp                | 488 ms                                                 | 522 ms: 1.07x slower                                       |
| html5lib                   | 64.5 ms                                                | 69.1 ms: 1.07x slower                                      |
| nqueens                    | 80.6 ms                                                | 86.5 ms: 1.07x slower                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 584 ms: 1.07x slower                                       |
| typing_runtime_protocols   | 159 us                                                 | 173 us: 1.09x slower                                       |
| hexiom                     | 6.13 ms                                                | 6.67 ms: 1.09x slower                                      |
| python_startup_no_site     | 6.99 ms                                                | 7.62 ms: 1.09x slower                                      |
| aiohttp                    | 1.14 ms                                                | 1.25 ms: 1.09x slower                                      |
| gunicorn                   | 1.23 ms                                                | 1.34 ms: 1.10x slower                                      |
| sympy_str                  | 274 ms                                                 | 302 ms: 1.10x slower                                       |
| sympy_expand               | 462 ms                                                 | 510 ms: 1.10x slower                                       |
| async_tree_io              | 843 ms                                                 | 932 ms: 1.11x slower                                       |
| coverage                   | 83.7 ms                                                | 92.7 ms: 1.11x slower                                      |
| dulwich_log                | 63.0 ms                                                | 69.7 ms: 1.11x slower                                      |
| scimark_lu                 | 115 ms                                                 | 127 ms: 1.11x slower                                       |
| genshi_text                | 22.9 ms                                                | 25.5 ms: 1.11x slower                                      |
| dask                       | 338 ms                                                 | 377 ms: 1.12x slower                                       |
| pylint                     | 313 ms                                                 | 353 ms: 1.13x slower                                       |
| sympy_integrate            | 19.9 ms                                                | 22.5 ms: 1.13x slower                                      |
| create_gc_cycles           | 1.61 ms                                                | 1.83 ms: 1.14x slower                                      |
| async_tree_io_tg           | 825 ms                                                 | 945 ms: 1.15x slower                                       |
| sympy_sum                  | 150 ms                                                 | 172 ms: 1.15x slower                                       |
| docutils                   | 2.58 sec                                               | 2.99 sec: 1.16x slower                                     |
| generators                 | 28.8 ms                                                | 33.5 ms: 1.16x slower                                      |
| deltablue                  | 3.15 ms                                                | 3.70 ms: 1.17x slower                                      |
| genshi_xml                 | 50.3 ms                                                | 60.2 ms: 1.20x slower                                      |
| Geometric mean             | (ref)                                                  | 1.03x slower                                               |

Benchmark hidden because not significant (7): bench_mp_pool, xml_etree_iterparse, pickle_pure_python, regex_v8, chaos, coroutines, async_tree_memoization
Ignored benchmarks (1) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: unpack_sequence

# HPT report

- Reliability score: 99.73% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x