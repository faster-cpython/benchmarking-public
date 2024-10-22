# Results vs. 3.13.0

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: c232e47
- commit date: 2024-08-07
- overall geometric mean: 1.04x slower
- HPT reliability: 52.53%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 282 ms: 1.07x slower                                                      |
| docutils       | 2.58 sec                                               | 6.89 sec: 2.67x slower                                                    |
| html5lib       | 64.5 ms                                                | 67.4 ms: 1.04x slower                                                     |
| tornado_http   | 91.5 ms                                                | 93.1 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                  | 1.32x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 398 ms: 1.17x faster                                                      |
| async_tree_none           | 354 ms                                                 | 331 ms: 1.07x faster                                                      |
| async_tree_none_tg        | 320 ms                                                 | 305 ms: 1.05x faster                                                      |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                    |
| asyncio_tcp               | 488 ms                                                 | 502 ms: 1.03x slower                                                      |
| async_generators          | 433 ms                                                 | 454 ms: 1.05x slower                                                      |
| async_tree_io_tg          | 825 ms                                                 | 880 ms: 1.07x slower                                                      |
| async_tree_io             | 843 ms                                                 | 914 ms: 1.08x slower                                                      |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (5): async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 71.0 ms: 1.11x faster                                                     |
| nbody          | 85.7 ms                                                | 79.4 ms: 1.08x faster                                                     |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.06x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 25.3 ms                                                | 24.7 ms: 1.02x faster                                                     |
| regex_effbot   | 3.88 ms                                                | 3.82 ms: 1.02x faster                                                     |
| regex_dna      | 220 ms                                                 | 224 ms: 1.02x slower                                                      |
| regex_compile  | 131 ms                                                 | 136 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                  | 1.00x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 1.89 sec: 1.12x faster                                                    |
| xml_etree_parse      | 156 ms                                                 | 147 ms: 1.06x faster                                                      |
| xml_etree_process    | 60.4 ms                                                | 57.8 ms: 1.04x faster                                                     |
| xml_etree_generate   | 87.0 ms                                                | 84.1 ms: 1.03x faster                                                     |
| xml_etree_iterparse  | 102 ms                                                 | 99.6 ms: 1.02x faster                                                     |
| json_dumps           | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                     |
| unpickle_pure_python | 213 us                                                 | 211 us: 1.01x faster                                                      |
| json_loads           | 27.0 us                                                | 28.0 us: 1.04x slower                                                     |
| pickle_pure_python   | 300 us                                                 | 316 us: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.01x slower                                                     |
| python_startup_no_site | 6.99 ms                                                | 7.20 ms: 1.03x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.71 ms: 1.14x faster                                                     |
| django_template | 34.4 ms                                                | 35.3 ms: 1.03x slower                                                     |
| genshi_text     | 22.9 ms                                                | 25.5 ms: 1.12x slower                                                     |
| genshi_xml      | 50.3 ms                                                | 57.1 ms: 1.14x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                              |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 27.5 us: 1.38x faster                                                     |
| deepcopy                  | 352 us                                                 | 260 us: 1.36x faster                                                      |
| richards                  | 48.1 ms                                                | 39.7 ms: 1.21x faster                                                     |
| scimark_fft               | 369 ms                                                 | 304 ms: 1.21x faster                                                      |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.15 ms: 1.21x faster                                                     |
| richards_super            | 54.4 ms                                                | 45.4 ms: 1.20x faster                                                     |
| deepcopy_reduce           | 3.17 us                                                | 2.68 us: 1.18x faster                                                     |
| async_tree_memoization_tg | 465 ms                                                 | 398 ms: 1.17x faster                                                      |
| spectral_norm             | 115 ms                                                 | 99.5 ms: 1.16x faster                                                     |
| mako                      | 11.1 ms                                                | 9.71 ms: 1.14x faster                                                     |
| tomli_loads               | 2.11 sec                                               | 1.89 sec: 1.12x faster                                                    |
| float                     | 78.5 ms                                                | 71.0 ms: 1.11x faster                                                     |
| crypto_pyaes              | 73.0 ms                                                | 66.1 ms: 1.10x faster                                                     |
| nbody                     | 85.7 ms                                                | 79.4 ms: 1.08x faster                                                     |
| telco                     | 8.45 ms                                                | 7.83 ms: 1.08x faster                                                     |
| scimark_lu                | 115 ms                                                 | 107 ms: 1.07x faster                                                      |
| pathlib                   | 17.1 ms                                                | 16.0 ms: 1.07x faster                                                     |
| async_tree_none           | 354 ms                                                 | 331 ms: 1.07x faster                                                      |
| scimark_sor               | 122 ms                                                 | 116 ms: 1.06x faster                                                      |
| xml_etree_parse           | 156 ms                                                 | 147 ms: 1.06x faster                                                      |
| scimark_monte_carlo       | 66.3 ms                                                | 62.8 ms: 1.06x faster                                                     |
| async_tree_none_tg        | 320 ms                                                 | 305 ms: 1.05x faster                                                      |
| xml_etree_process         | 60.4 ms                                                | 57.8 ms: 1.04x faster                                                     |
| logging_format            | 6.25 us                                                | 6.01 us: 1.04x faster                                                     |
| bpe_tokeniser             | 4.69 sec                                               | 4.52 sec: 1.04x faster                                                    |
| logging_simple            | 5.66 us                                                | 5.47 us: 1.04x faster                                                     |
| xml_etree_generate        | 87.0 ms                                                | 84.1 ms: 1.03x faster                                                     |
| pyflate                   | 460 ms                                                 | 445 ms: 1.03x faster                                                      |
| deltablue                 | 3.15 ms                                                | 3.06 ms: 1.03x faster                                                     |
| regex_v8                  | 25.3 ms                                                | 24.7 ms: 1.02x faster                                                     |
| xml_etree_iterparse       | 102 ms                                                 | 99.6 ms: 1.02x faster                                                     |
| fannkuch                  | 381 ms                                                 | 372 ms: 1.02x faster                                                      |
| logging_silent            | 102 ns                                                 | 99.8 ns: 1.02x faster                                                     |
| json                      | 5.20 ms                                                | 5.08 ms: 1.02x faster                                                     |
| mdp                       | 2.74 sec                                               | 2.70 sec: 1.02x faster                                                    |
| regex_effbot              | 3.88 ms                                                | 3.82 ms: 1.02x faster                                                     |
| gc_traversal              | 3.81 ms                                                | 3.75 ms: 1.02x faster                                                     |
| pprint_safe_repr          | 744 ms                                                 | 733 ms: 1.02x faster                                                      |
| json_dumps                | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                     |
| meteor_contest            | 108 ms                                                 | 106 ms: 1.01x faster                                                      |
| unpickle_pure_python      | 213 us                                                 | 211 us: 1.01x faster                                                      |
| pidigits                  | 186 ms                                                 | 186 ms: 1.00x faster                                                      |
| bench_thread_pool         | 815 us                                                 | 817 us: 1.00x slower                                                      |
| python_startup            | 10.6 ms                                                | 10.6 ms: 1.01x slower                                                     |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                    |
| tornado_http              | 91.5 ms                                                | 93.1 ms: 1.02x slower                                                     |
| regex_dna                 | 220 ms                                                 | 224 ms: 1.02x slower                                                      |
| pprint_pformat            | 1.51 sec                                               | 1.54 sec: 1.02x slower                                                    |
| go                        | 142 ms                                                 | 144 ms: 1.02x slower                                                      |
| django_template           | 34.4 ms                                                | 35.3 ms: 1.03x slower                                                     |
| asyncio_tcp               | 488 ms                                                 | 502 ms: 1.03x slower                                                      |
| python_startup_no_site    | 6.99 ms                                                | 7.20 ms: 1.03x slower                                                     |
| regex_compile             | 131 ms                                                 | 136 ms: 1.04x slower                                                      |
| json_loads                | 27.0 us                                                | 28.0 us: 1.04x slower                                                     |
| html5lib                  | 64.5 ms                                                | 67.4 ms: 1.04x slower                                                     |
| sqlglot_normalize         | 107 ms                                                 | 113 ms: 1.05x slower                                                      |
| async_generators          | 433 ms                                                 | 454 ms: 1.05x slower                                                      |
| pickle_pure_python        | 300 us                                                 | 316 us: 1.05x slower                                                      |
| 2to3                      | 265 ms                                                 | 282 ms: 1.07x slower                                                      |
| async_tree_io_tg          | 825 ms                                                 | 880 ms: 1.07x slower                                                      |
| nqueens                   | 80.6 ms                                                | 86.3 ms: 1.07x slower                                                     |
| typing_runtime_protocols  | 159 us                                                 | 170 us: 1.07x slower                                                      |
| sympy_expand              | 462 ms                                                 | 496 ms: 1.07x slower                                                      |
| sympy_str                 | 274 ms                                                 | 296 ms: 1.08x slower                                                      |
| async_tree_io             | 843 ms                                                 | 914 ms: 1.08x slower                                                      |
| coverage                  | 83.7 ms                                                | 91.4 ms: 1.09x slower                                                     |
| hexiom                    | 6.13 ms                                                | 6.71 ms: 1.10x slower                                                     |
| sqlglot_transpile         | 1.57 ms                                                | 1.73 ms: 1.10x slower                                                     |
| create_gc_cycles          | 1.61 ms                                                | 1.78 ms: 1.11x slower                                                     |
| sqlglot_parse             | 1.27 ms                                                | 1.40 ms: 1.11x slower                                                     |
| genshi_text               | 22.9 ms                                                | 25.5 ms: 1.12x slower                                                     |
| sqlglot_optimize          | 53.9 ms                                                | 60.6 ms: 1.12x slower                                                     |
| genshi_xml                | 50.3 ms                                                | 57.1 ms: 1.14x slower                                                     |
| generators                | 28.8 ms                                                | 32.8 ms: 1.14x slower                                                     |
| sympy_sum                 | 150 ms                                                 | 171 ms: 1.14x slower                                                      |
| sympy_integrate           | 19.9 ms                                                | 22.8 ms: 1.15x slower                                                     |
| pycparser                 | 1.19 sec                                               | 1.64 sec: 1.37x slower                                                    |
| pylint                    | 313 ms                                                 | 443 ms: 1.41x slower                                                      |
| docutils                  | 2.58 sec                                               | 6.89 sec: 2.67x slower                                                    |
| raytrace                  | 262 ms                                                 | 5.00 sec: 19.13x slower                                                   |
| Geometric mean            | (ref)                                                  | 1.04x slower                                                              |

Benchmark hidden because not significant (9): async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, chaos, comprehensions, bench_mp_pool, asyncio_websockets, thrift, coroutines
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 52.53% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.10x