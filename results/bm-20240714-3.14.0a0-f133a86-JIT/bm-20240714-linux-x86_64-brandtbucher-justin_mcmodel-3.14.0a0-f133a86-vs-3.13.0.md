# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_mcmodel
- machine: linux-x86_64
- commit hash: f133a86
- commit date: 2024-07-14
- overall geometric mean: 1.01x faster
- HPT reliability: 58.07%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 269 ms: 1.01x slower                                                  |
| docutils       | 2.58 sec                                               | 2.86 sec: 1.11x slower                                                |
| html5lib       | 64.5 ms                                                | 65.6 ms: 1.02x slower                                                 |
| tornado_http   | 91.5 ms                                                | 93.2 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86 |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 376 ms: 1.24x faster                                                  |
| async_tree_none           | 354 ms                                                 | 324 ms: 1.09x faster                                                  |
| async_tree_memoization    | 442 ms                                                 | 408 ms: 1.08x faster                                                  |
| async_tree_none_tg        | 320 ms                                                 | 300 ms: 1.07x faster                                                  |
| asyncio_websockets        | 555 ms                                                 | 558 ms: 1.00x slower                                                  |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                |
| async_tree_io_tg          | 825 ms                                                 | 847 ms: 1.03x slower                                                  |
| asyncio_tcp               | 488 ms                                                 | 502 ms: 1.03x slower                                                  |
| coroutines                | 22.5 ms                                                | 24.0 ms: 1.06x slower                                                 |
| async_generators          | 433 ms                                                 | 463 ms: 1.07x slower                                                  |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 69.6 ms: 1.13x faster                                                 |
| nbody          | 85.7 ms                                                | 77.1 ms: 1.11x faster                                                 |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 25.3 ms                                                | 23.7 ms: 1.07x faster                                                 |
| regex_effbot   | 3.88 ms                                                | 3.67 ms: 1.06x faster                                                 |
| regex_compile  | 131 ms                                                 | 134 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 1.91 sec: 1.10x faster                                                |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.05x faster                                                  |
| xml_etree_generate   | 87.0 ms                                                | 84.2 ms: 1.03x faster                                                 |
| xml_etree_process    | 60.4 ms                                                | 58.8 ms: 1.03x faster                                                 |
| xml_etree_iterparse  | 102 ms                                                 | 99.9 ms: 1.02x faster                                                 |
| pickle_pure_python   | 300 us                                                 | 294 us: 1.02x faster                                                  |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                 |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                                  |
| json_loads           | 27.0 us                                                | 27.5 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                 |
| python_startup_no_site | 6.99 ms                                                | 7.13 ms: 1.02x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.85 ms: 1.13x faster                                                 |
| django_template | 34.4 ms                                                | 35.1 ms: 1.02x slower                                                 |
| genshi_text     | 22.9 ms                                                | 24.1 ms: 1.05x slower                                                 |
| genshi_xml      | 50.3 ms                                                | 56.1 ms: 1.11x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86 |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 28.2 us: 1.35x faster                                                 |
| deepcopy                  | 352 us                                                 | 271 us: 1.30x faster                                                  |
| async_tree_memoization_tg | 465 ms                                                 | 376 ms: 1.24x faster                                                  |
| richards                  | 48.1 ms                                                | 40.8 ms: 1.18x faster                                                 |
| deepcopy_reduce           | 3.17 us                                                | 2.70 us: 1.17x faster                                                 |
| richards_super            | 54.4 ms                                                | 46.8 ms: 1.16x faster                                                 |
| scimark_fft               | 369 ms                                                 | 322 ms: 1.14x faster                                                  |
| float                     | 78.5 ms                                                | 69.6 ms: 1.13x faster                                                 |
| mako                      | 11.1 ms                                                | 9.85 ms: 1.13x faster                                                 |
| nbody                     | 85.7 ms                                                | 77.1 ms: 1.11x faster                                                 |
| tomli_loads               | 2.11 sec                                               | 1.91 sec: 1.10x faster                                                |
| scimark_monte_carlo       | 66.3 ms                                                | 60.3 ms: 1.10x faster                                                 |
| async_tree_none           | 354 ms                                                 | 324 ms: 1.09x faster                                                  |
| crypto_pyaes              | 73.0 ms                                                | 66.9 ms: 1.09x faster                                                 |
| async_tree_memoization    | 442 ms                                                 | 408 ms: 1.08x faster                                                  |
| spectral_norm             | 115 ms                                                 | 107 ms: 1.08x faster                                                  |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.70 ms: 1.07x faster                                                 |
| async_tree_none_tg        | 320 ms                                                 | 300 ms: 1.07x faster                                                  |
| regex_v8                  | 25.3 ms                                                | 23.7 ms: 1.07x faster                                                 |
| pathlib                   | 17.1 ms                                                | 16.0 ms: 1.07x faster                                                 |
| pycparser                 | 1.19 sec                                               | 1.12 sec: 1.06x faster                                                |
| regex_effbot              | 3.88 ms                                                | 3.67 ms: 1.06x faster                                                 |
| xml_etree_parse           | 156 ms                                                 | 148 ms: 1.05x faster                                                  |
| mdp                       | 2.74 sec                                               | 2.61 sec: 1.05x faster                                                |
| telco                     | 8.45 ms                                                | 8.09 ms: 1.04x faster                                                 |
| fannkuch                  | 381 ms                                                 | 365 ms: 1.04x faster                                                  |
| logging_simple            | 5.66 us                                                | 5.45 us: 1.04x faster                                                 |
| logging_format            | 6.25 us                                                | 6.04 us: 1.04x faster                                                 |
| pyflate                   | 460 ms                                                 | 445 ms: 1.03x faster                                                  |
| xml_etree_generate        | 87.0 ms                                                | 84.2 ms: 1.03x faster                                                 |
| pprint_pformat            | 1.51 sec                                               | 1.47 sec: 1.03x faster                                                |
| pprint_safe_repr          | 744 ms                                                 | 724 ms: 1.03x faster                                                  |
| xml_etree_process         | 60.4 ms                                                | 58.8 ms: 1.03x faster                                                 |
| xml_etree_iterparse       | 102 ms                                                 | 99.9 ms: 1.02x faster                                                 |
| pickle_pure_python        | 300 us                                                 | 294 us: 1.02x faster                                                  |
| chaos                     | 58.4 ms                                                | 57.4 ms: 1.02x faster                                                 |
| json                      | 5.20 ms                                                | 5.15 ms: 1.01x faster                                                 |
| gc_traversal              | 3.81 ms                                                | 3.78 ms: 1.01x faster                                                 |
| sqlglot_parse             | 1.27 ms                                                | 1.26 ms: 1.01x faster                                                 |
| pidigits                  | 186 ms                                                 | 185 ms: 1.00x faster                                                  |
| meteor_contest            | 108 ms                                                 | 107 ms: 1.00x faster                                                  |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                 |
| asyncio_websockets        | 555 ms                                                 | 558 ms: 1.00x slower                                                  |
| json_dumps                | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                 |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                |
| go                        | 142 ms                                                 | 143 ms: 1.01x slower                                                  |
| sqlglot_optimize          | 53.9 ms                                                | 54.6 ms: 1.01x slower                                                 |
| unpickle_pure_python      | 213 us                                                 | 216 us: 1.01x slower                                                  |
| 2to3                      | 265 ms                                                 | 269 ms: 1.01x slower                                                  |
| html5lib                  | 64.5 ms                                                | 65.6 ms: 1.02x slower                                                 |
| tornado_http              | 91.5 ms                                                | 93.2 ms: 1.02x slower                                                 |
| thrift                    | 796 us                                                 | 811 us: 1.02x slower                                                  |
| json_loads                | 27.0 us                                                | 27.5 us: 1.02x slower                                                 |
| python_startup_no_site    | 6.99 ms                                                | 7.13 ms: 1.02x slower                                                 |
| regex_compile             | 131 ms                                                 | 134 ms: 1.02x slower                                                  |
| comprehensions            | 16.4 us                                                | 16.7 us: 1.02x slower                                                 |
| django_template           | 34.4 ms                                                | 35.1 ms: 1.02x slower                                                 |
| bench_thread_pool         | 815 us                                                 | 836 us: 1.03x slower                                                  |
| async_tree_io_tg          | 825 ms                                                 | 847 ms: 1.03x slower                                                  |
| asyncio_tcp               | 488 ms                                                 | 502 ms: 1.03x slower                                                  |
| bpe_tokeniser             | 4.69 sec                                               | 4.82 sec: 1.03x slower                                                |
| sqlglot_normalize         | 107 ms                                                 | 111 ms: 1.03x slower                                                  |
| generators                | 28.8 ms                                                | 29.8 ms: 1.03x slower                                                 |
| raytrace                  | 262 ms                                                 | 271 ms: 1.04x slower                                                  |
| logging_silent            | 102 ns                                                 | 106 ns: 1.04x slower                                                  |
| genshi_text               | 22.9 ms                                                | 24.1 ms: 1.05x slower                                                 |
| typing_runtime_protocols  | 159 us                                                 | 168 us: 1.05x slower                                                  |
| scimark_sor               | 122 ms                                                 | 129 ms: 1.05x slower                                                  |
| hexiom                    | 6.13 ms                                                | 6.47 ms: 1.06x slower                                                 |
| sympy_str                 | 274 ms                                                 | 291 ms: 1.06x slower                                                  |
| coroutines                | 22.5 ms                                                | 24.0 ms: 1.06x slower                                                 |
| nqueens                   | 80.6 ms                                                | 85.8 ms: 1.06x slower                                                 |
| sympy_expand              | 462 ms                                                 | 492 ms: 1.07x slower                                                  |
| pylint                    | 313 ms                                                 | 334 ms: 1.07x slower                                                  |
| async_generators          | 433 ms                                                 | 463 ms: 1.07x slower                                                  |
| dulwich_log               | 63.0 ms                                                | 67.4 ms: 1.07x slower                                                 |
| dask                      | 338 ms                                                 | 361 ms: 1.07x slower                                                  |
| sympy_integrate           | 19.9 ms                                                | 21.7 ms: 1.09x slower                                                 |
| scimark_lu                | 115 ms                                                 | 126 ms: 1.10x slower                                                  |
| sympy_sum                 | 150 ms                                                 | 165 ms: 1.10x slower                                                  |
| create_gc_cycles          | 1.61 ms                                                | 1.77 ms: 1.10x slower                                                 |
| coverage                  | 83.7 ms                                                | 92.7 ms: 1.11x slower                                                 |
| docutils                  | 2.58 sec                                               | 2.86 sec: 1.11x slower                                                |
| genshi_xml                | 50.3 ms                                                | 56.1 ms: 1.11x slower                                                 |
| deltablue                 | 3.15 ms                                                | 3.54 ms: 1.13x slower                                                 |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, regex_dna, bench_mp_pool, sqlglot_transpile, async_tree_io
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 58.07% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x