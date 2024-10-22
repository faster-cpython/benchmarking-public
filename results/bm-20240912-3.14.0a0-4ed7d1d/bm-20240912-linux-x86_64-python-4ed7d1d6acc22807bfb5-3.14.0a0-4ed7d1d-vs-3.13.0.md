# Results vs. 3.13.0

- fork: python
- ref: 4ed7d1d6acc22807bfb5
- machine: linux-x86_64
- commit hash: 4ed7d1d
- commit date: 2024-09-12
- overall geometric mean: 1.02x faster
- HPT reliability: 99.91%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 254 ms: 1.04x faster                                                  |
| docutils       | 2.58 sec                                               | 2.66 sec: 1.03x slower                                                |
| html5lib       | 64.5 ms                                                | 63.3 ms: 1.02x faster                                                 |
| tornado_http   | 91.5 ms                                                | 90.8 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 386 ms: 1.20x faster                                                  |
| async_tree_none            | 354 ms                                                 | 314 ms: 1.13x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 395 ms: 1.12x faster                                                  |
| async_tree_none_tg         | 320 ms                                                 | 305 ms: 1.05x faster                                                  |
| asyncio_tcp                | 488 ms                                                 | 472 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 566 ms: 1.01x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 554 ms: 1.02x slower                                                  |
| async_tree_io              | 843 ms                                                 | 864 ms: 1.03x slower                                                  |
| coroutines                 | 22.5 ms                                                | 23.2 ms: 1.03x slower                                                 |
| async_tree_io_tg           | 825 ms                                                 | 875 ms: 1.06x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (3): asyncio_websockets, async_generators, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 78.1 ms: 1.00x faster                                                 |
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                  |
| nbody          | 85.7 ms                                                | 86.5 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.72 ms: 1.04x faster                                                 |
| regex_v8       | 25.3 ms                                                | 24.6 ms: 1.03x faster                                                 |
| regex_compile  | 131 ms                                                 | 128 ms: 1.02x faster                                                  |
| regex_dna      | 220 ms                                                 | 218 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_process    | 60.4 ms                                                | 58.9 ms: 1.02x faster                                                 |
| xml_etree_generate   | 87.0 ms                                                | 85.0 ms: 1.02x faster                                                 |
| xml_etree_parse      | 156 ms                                                 | 154 ms: 1.01x faster                                                  |
| json_loads           | 27.0 us                                                | 26.7 us: 1.01x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 211 us: 1.01x faster                                                  |
| pickle               | 11.6 us                                                | 11.5 us: 1.01x faster                                                 |
| pickle_pure_python   | 300 us                                                 | 303 us: 1.01x slower                                                  |
| xml_etree_iterparse  | 102 ms                                                 | 104 ms: 1.02x slower                                                  |
| pickle_dict          | 33.2 us                                                | 33.9 us: 1.02x slower                                                 |
| pickle_list          | 5.01 us                                                | 5.14 us: 1.03x slower                                                 |
| unpickle_list        | 4.96 us                                                | 5.17 us: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (3): tomli_loads, json_dumps, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                 |
| python_startup_no_site | 6.99 ms                                                | 6.99 ms: 1.00x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 34.4 ms                                                | 34.1 ms: 1.01x faster                                                 |
| mako            | 11.1 ms                                                | 11.1 ms: 1.00x slower                                                 |
| genshi_xml      | 50.3 ms                                                | 50.9 ms: 1.01x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 257 us: 1.37x faster                                                  |
| deepcopy_memo              | 38.0 us                                                | 29.7 us: 1.28x faster                                                 |
| go                         | 142 ms                                                 | 118 ms: 1.20x faster                                                  |
| async_tree_memoization_tg  | 465 ms                                                 | 386 ms: 1.20x faster                                                  |
| deepcopy_reduce            | 3.17 us                                                | 2.65 us: 1.20x faster                                                 |
| async_tree_none            | 354 ms                                                 | 314 ms: 1.13x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 395 ms: 1.12x faster                                                  |
| pathlib                    | 17.1 ms                                                | 15.8 ms: 1.08x faster                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.67 ms: 1.08x faster                                                 |
| pycparser                  | 1.19 sec                                               | 1.13 sec: 1.06x faster                                                |
| async_tree_none_tg         | 320 ms                                                 | 305 ms: 1.05x faster                                                  |
| json                       | 5.20 ms                                                | 4.96 ms: 1.05x faster                                                 |
| generators                 | 28.8 ms                                                | 27.5 ms: 1.05x faster                                                 |
| regex_effbot               | 3.88 ms                                                | 3.72 ms: 1.04x faster                                                 |
| 2to3                       | 265 ms                                                 | 254 ms: 1.04x faster                                                  |
| thrift                     | 796 us                                                 | 764 us: 1.04x faster                                                  |
| logging_silent             | 102 ns                                                 | 98.2 ns: 1.04x faster                                                 |
| asyncio_tcp                | 488 ms                                                 | 472 ms: 1.03x faster                                                  |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.03x faster                                                  |
| mdp                        | 2.74 sec                                               | 2.65 sec: 1.03x faster                                                |
| richards_super             | 54.4 ms                                                | 52.7 ms: 1.03x faster                                                 |
| richards                   | 48.1 ms                                                | 46.8 ms: 1.03x faster                                                 |
| bench_thread_pool          | 815 us                                                 | 792 us: 1.03x faster                                                  |
| regex_v8                   | 25.3 ms                                                | 24.6 ms: 1.03x faster                                                 |
| pprint_safe_repr           | 744 ms                                                 | 725 ms: 1.03x faster                                                  |
| xml_etree_process          | 60.4 ms                                                | 58.9 ms: 1.02x faster                                                 |
| pprint_pformat             | 1.51 sec                                               | 1.48 sec: 1.02x faster                                                |
| regex_compile              | 131 ms                                                 | 128 ms: 1.02x faster                                                  |
| xml_etree_generate         | 87.0 ms                                                | 85.0 ms: 1.02x faster                                                 |
| scimark_lu                 | 115 ms                                                 | 113 ms: 1.02x faster                                                  |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                  |
| html5lib                   | 64.5 ms                                                | 63.3 ms: 1.02x faster                                                 |
| scimark_fft                | 369 ms                                                 | 362 ms: 1.02x faster                                                  |
| crypto_pyaes               | 73.0 ms                                                | 71.7 ms: 1.02x faster                                                 |
| sympy_str                  | 274 ms                                                 | 269 ms: 1.02x faster                                                  |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.01x faster                                                  |
| xml_etree_parse            | 156 ms                                                 | 154 ms: 1.01x faster                                                  |
| sqlglot_optimize           | 53.9 ms                                                | 53.2 ms: 1.01x faster                                                 |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 566 ms: 1.01x faster                                                  |
| sympy_integrate            | 19.9 ms                                                | 19.6 ms: 1.01x faster                                                 |
| sympy_expand               | 462 ms                                                 | 456 ms: 1.01x faster                                                  |
| pyflate                    | 460 ms                                                 | 454 ms: 1.01x faster                                                  |
| json_loads                 | 27.0 us                                                | 26.7 us: 1.01x faster                                                 |
| raytrace                   | 262 ms                                                 | 259 ms: 1.01x faster                                                  |
| logging_simple             | 5.66 us                                                | 5.61 us: 1.01x faster                                                 |
| unpickle_pure_python       | 213 us                                                 | 211 us: 1.01x faster                                                  |
| django_template            | 34.4 ms                                                | 34.1 ms: 1.01x faster                                                 |
| pickle                     | 11.6 us                                                | 11.5 us: 1.01x faster                                                 |
| tornado_http               | 91.5 ms                                                | 90.8 ms: 1.01x faster                                                 |
| regex_dna                  | 220 ms                                                 | 218 ms: 1.01x faster                                                  |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                 |
| float                      | 78.5 ms                                                | 78.1 ms: 1.00x faster                                                 |
| python_startup_no_site     | 6.99 ms                                                | 6.99 ms: 1.00x slower                                                 |
| mako                       | 11.1 ms                                                | 11.1 ms: 1.00x slower                                                 |
| sqlglot_transpile          | 1.57 ms                                                | 1.58 ms: 1.01x slower                                                 |
| pidigits                   | 186 ms                                                 | 187 ms: 1.01x slower                                                  |
| hexiom                     | 6.13 ms                                                | 6.17 ms: 1.01x slower                                                 |
| nbody                      | 85.7 ms                                                | 86.5 ms: 1.01x slower                                                 |
| telco                      | 8.45 ms                                                | 8.53 ms: 1.01x slower                                                 |
| coverage                   | 83.7 ms                                                | 84.6 ms: 1.01x slower                                                 |
| pickle_pure_python         | 300 us                                                 | 303 us: 1.01x slower                                                  |
| genshi_xml                 | 50.3 ms                                                | 50.9 ms: 1.01x slower                                                 |
| scimark_monte_carlo        | 66.3 ms                                                | 67.1 ms: 1.01x slower                                                 |
| sqlglot_parse              | 1.27 ms                                                | 1.28 ms: 1.01x slower                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 554 ms: 1.02x slower                                                  |
| typing_runtime_protocols   | 159 us                                                 | 162 us: 1.02x slower                                                  |
| xml_etree_iterparse        | 102 ms                                                 | 104 ms: 1.02x slower                                                  |
| deltablue                  | 3.15 ms                                                | 3.22 ms: 1.02x slower                                                 |
| pickle_dict                | 33.2 us                                                | 33.9 us: 1.02x slower                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 4.80 sec: 1.02x slower                                                |
| async_tree_io              | 843 ms                                                 | 864 ms: 1.03x slower                                                  |
| pickle_list                | 5.01 us                                                | 5.14 us: 1.03x slower                                                 |
| dulwich_log                | 63.0 ms                                                | 64.6 ms: 1.03x slower                                                 |
| docutils                   | 2.58 sec                                               | 2.66 sec: 1.03x slower                                                |
| coroutines                 | 22.5 ms                                                | 23.2 ms: 1.03x slower                                                 |
| scimark_sor                | 122 ms                                                 | 126 ms: 1.03x slower                                                  |
| unpickle_list              | 4.96 us                                                | 5.17 us: 1.04x slower                                                 |
| fannkuch                   | 381 ms                                                 | 397 ms: 1.04x slower                                                  |
| gc_traversal               | 3.81 ms                                                | 3.98 ms: 1.04x slower                                                 |
| async_tree_io_tg           | 825 ms                                                 | 875 ms: 1.06x slower                                                  |
| create_gc_cycles           | 1.61 ms                                                | 1.73 ms: 1.07x slower                                                 |
| unpack_sequence            | 42.4 ns                                                | 45.7 ns: 1.08x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (15): logging_format, genshi_text, tomli_loads, comprehensions, json_dumps, asyncio_websockets, nqueens, async_generators, asyncio_tcp_ssl, bench_mp_pool, sqlglot_normalize, chaos, unpickle, sqlite_synth, pylint
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 99.91% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x