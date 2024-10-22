# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_mcmodel
- machine: linux-x86_64
- commit hash: d19b26c
- commit date: 2024-07-14
- overall geometric mean: 1.02x faster
- HPT reliability: 66.38%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 268 ms: 1.01x slower                                                  |
| docutils       | 2.58 sec                                               | 2.83 sec: 1.09x slower                                                |
| html5lib       | 64.5 ms                                                | 65.4 ms: 1.01x slower                                                 |
| tornado_http   | 91.5 ms                                                | 92.1 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 376 ms: 1.24x faster                                                  |
| async_tree_none            | 354 ms                                                 | 324 ms: 1.09x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 407 ms: 1.09x faster                                                  |
| async_tree_none_tg         | 320 ms                                                 | 300 ms: 1.07x faster                                                  |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 561 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 538 ms: 1.01x faster                                                  |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.01x slower                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                |
| async_tree_io_tg           | 825 ms                                                 | 847 ms: 1.03x slower                                                  |
| asyncio_tcp                | 488 ms                                                 | 501 ms: 1.03x slower                                                  |
| coroutines                 | 22.5 ms                                                | 23.3 ms: 1.03x slower                                                 |
| async_generators           | 433 ms                                                 | 455 ms: 1.05x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 85.7 ms                                                | 75.6 ms: 1.13x faster                                                 |
| float          | 78.5 ms                                                | 69.7 ms: 1.13x faster                                                 |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.64 ms: 1.07x faster                                                 |
| regex_v8       | 25.3 ms                                                | 24.5 ms: 1.03x faster                                                 |
| regex_compile  | 131 ms                                                 | 132 ms: 1.01x slower                                                  |
| regex_dna      | 220 ms                                                 | 230 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 1.92 sec: 1.10x faster                                                |
| xml_etree_generate   | 87.0 ms                                                | 81.7 ms: 1.07x faster                                                 |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.06x faster                                                  |
| xml_etree_process    | 60.4 ms                                                | 57.7 ms: 1.05x faster                                                 |
| xml_etree_iterparse  | 102 ms                                                 | 99.0 ms: 1.03x faster                                                 |
| pickle_pure_python   | 300 us                                                 | 295 us: 1.02x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                  |
| json_loads           | 27.0 us                                                | 27.7 us: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                 |
| python_startup_no_site | 6.99 ms                                                | 7.12 ms: 1.02x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.73 ms: 1.14x faster                                                 |
| genshi_text     | 22.9 ms                                                | 23.8 ms: 1.04x slower                                                 |
| django_template | 34.4 ms                                                | 35.8 ms: 1.04x slower                                                 |
| genshi_xml      | 50.3 ms                                                | 55.6 ms: 1.10x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 27.9 us: 1.36x faster                                                 |
| deepcopy                   | 352 us                                                 | 269 us: 1.31x faster                                                  |
| async_tree_memoization_tg  | 465 ms                                                 | 376 ms: 1.24x faster                                                  |
| richards_super             | 54.4 ms                                                | 45.8 ms: 1.19x faster                                                 |
| richards                   | 48.1 ms                                                | 40.5 ms: 1.19x faster                                                 |
| scimark_fft                | 369 ms                                                 | 316 ms: 1.17x faster                                                  |
| deepcopy_reduce            | 3.17 us                                                | 2.75 us: 1.15x faster                                                 |
| mako                       | 11.1 ms                                                | 9.73 ms: 1.14x faster                                                 |
| nbody                      | 85.7 ms                                                | 75.6 ms: 1.13x faster                                                 |
| float                      | 78.5 ms                                                | 69.7 ms: 1.13x faster                                                 |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.11x faster                                                  |
| tomli_loads                | 2.11 sec                                               | 1.92 sec: 1.10x faster                                                |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.57 ms: 1.10x faster                                                 |
| scimark_monte_carlo        | 66.3 ms                                                | 60.6 ms: 1.09x faster                                                 |
| crypto_pyaes               | 73.0 ms                                                | 66.8 ms: 1.09x faster                                                 |
| async_tree_none            | 354 ms                                                 | 324 ms: 1.09x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 407 ms: 1.09x faster                                                  |
| mdp                        | 2.74 sec                                               | 2.56 sec: 1.07x faster                                                |
| pyflate                    | 460 ms                                                 | 429 ms: 1.07x faster                                                  |
| pycparser                  | 1.19 sec                                               | 1.12 sec: 1.07x faster                                                |
| async_tree_none_tg         | 320 ms                                                 | 300 ms: 1.07x faster                                                  |
| regex_effbot               | 3.88 ms                                                | 3.64 ms: 1.07x faster                                                 |
| xml_etree_generate         | 87.0 ms                                                | 81.7 ms: 1.07x faster                                                 |
| pathlib                    | 17.1 ms                                                | 16.0 ms: 1.06x faster                                                 |
| xml_etree_parse            | 156 ms                                                 | 148 ms: 1.06x faster                                                  |
| pprint_safe_repr           | 744 ms                                                 | 710 ms: 1.05x faster                                                  |
| xml_etree_process          | 60.4 ms                                                | 57.7 ms: 1.05x faster                                                 |
| logging_simple             | 5.66 us                                                | 5.42 us: 1.04x faster                                                 |
| logging_format             | 6.25 us                                                | 5.99 us: 1.04x faster                                                 |
| pprint_pformat             | 1.51 sec                                               | 1.46 sec: 1.04x faster                                                |
| xml_etree_iterparse        | 102 ms                                                 | 99.0 ms: 1.03x faster                                                 |
| regex_v8                   | 25.3 ms                                                | 24.5 ms: 1.03x faster                                                 |
| telco                      | 8.45 ms                                                | 8.23 ms: 1.03x faster                                                 |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 561 ms: 1.02x faster                                                  |
| json                       | 5.20 ms                                                | 5.09 ms: 1.02x faster                                                 |
| pickle_pure_python         | 300 us                                                 | 295 us: 1.02x faster                                                  |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.01x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 538 ms: 1.01x faster                                                  |
| sqlglot_parse              | 1.27 ms                                                | 1.26 ms: 1.01x faster                                                 |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                 |
| go                         | 142 ms                                                 | 141 ms: 1.00x faster                                                  |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                  |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.01x slower                                                  |
| tornado_http               | 91.5 ms                                                | 92.1 ms: 1.01x slower                                                 |
| comprehensions             | 16.4 us                                                | 16.5 us: 1.01x slower                                                 |
| regex_compile              | 131 ms                                                 | 132 ms: 1.01x slower                                                  |
| thrift                     | 796 us                                                 | 804 us: 1.01x slower                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                |
| 2to3                       | 265 ms                                                 | 268 ms: 1.01x slower                                                  |
| html5lib                   | 64.5 ms                                                | 65.4 ms: 1.01x slower                                                 |
| sqlglot_optimize           | 53.9 ms                                                | 54.9 ms: 1.02x slower                                                 |
| python_startup_no_site     | 6.99 ms                                                | 7.12 ms: 1.02x slower                                                 |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                                  |
| gc_traversal               | 3.81 ms                                                | 3.88 ms: 1.02x slower                                                 |
| raytrace                   | 262 ms                                                 | 268 ms: 1.02x slower                                                  |
| bench_thread_pool          | 815 us                                                 | 834 us: 1.02x slower                                                  |
| async_tree_io_tg           | 825 ms                                                 | 847 ms: 1.03x slower                                                  |
| json_loads                 | 27.0 us                                                | 27.7 us: 1.03x slower                                                 |
| asyncio_tcp                | 488 ms                                                 | 501 ms: 1.03x slower                                                  |
| generators                 | 28.8 ms                                                | 29.7 ms: 1.03x slower                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 4.84 sec: 1.03x slower                                                |
| coroutines                 | 22.5 ms                                                | 23.3 ms: 1.03x slower                                                 |
| sqlglot_normalize          | 107 ms                                                 | 111 ms: 1.04x slower                                                  |
| genshi_text                | 22.9 ms                                                | 23.8 ms: 1.04x slower                                                 |
| django_template            | 34.4 ms                                                | 35.8 ms: 1.04x slower                                                 |
| logging_silent             | 102 ns                                                 | 107 ns: 1.05x slower                                                  |
| regex_dna                  | 220 ms                                                 | 230 ms: 1.05x slower                                                  |
| async_generators           | 433 ms                                                 | 455 ms: 1.05x slower                                                  |
| hexiom                     | 6.13 ms                                                | 6.45 ms: 1.05x slower                                                 |
| sympy_str                  | 274 ms                                                 | 289 ms: 1.06x slower                                                  |
| sympy_expand               | 462 ms                                                 | 488 ms: 1.06x slower                                                  |
| typing_runtime_protocols   | 159 us                                                 | 169 us: 1.06x slower                                                  |
| dulwich_log                | 63.0 ms                                                | 67.3 ms: 1.07x slower                                                 |
| nqueens                    | 80.6 ms                                                | 86.2 ms: 1.07x slower                                                 |
| scimark_sor                | 122 ms                                                 | 131 ms: 1.07x slower                                                  |
| dask                       | 338 ms                                                 | 362 ms: 1.07x slower                                                  |
| sympy_sum                  | 150 ms                                                 | 163 ms: 1.09x slower                                                  |
| sympy_integrate            | 19.9 ms                                                | 21.7 ms: 1.09x slower                                                 |
| docutils                   | 2.58 sec                                               | 2.83 sec: 1.09x slower                                                |
| scimark_lu                 | 115 ms                                                 | 126 ms: 1.10x slower                                                  |
| coverage                   | 83.7 ms                                                | 92.5 ms: 1.10x slower                                                 |
| genshi_xml                 | 50.3 ms                                                | 55.6 ms: 1.10x slower                                                 |
| create_gc_cycles           | 1.61 ms                                                | 1.78 ms: 1.11x slower                                                 |
| deltablue                  | 3.15 ms                                                | 3.55 ms: 1.13x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (7): chaos, fannkuch, sqlglot_transpile, bench_mp_pool, async_tree_io, json_dumps, pylint
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 66.38% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x