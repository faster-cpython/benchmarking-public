# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_compact_exits
- machine: linux-x86_64
- commit hash: f2327f4
- commit date: 2024-09-18
- overall geometric mean: 1.03x faster
- HPT reliability: 92.50%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 282 ms: 1.03x slower                                                        |
| docutils       | 2.83 sec                                                   | 3.20 sec: 1.13x slower                                                      |
| html5lib       | 67.2 ms                                                    | 66.5 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                      | 1.04x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 360 ms: 1.05x faster                                                        |
| async_tree_io_tg           | 936 ms                                                     | 1.02 sec: 1.09x slower                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 666 ms: 1.13x slower                                                        |
| async_tree_memoization_tg  | 444 ms                                                     | 513 ms: 1.16x slower                                                        |
| async_tree_none_tg         | 336 ms                                                     | 401 ms: 1.19x slower                                                        |
| Geometric mean             | (ref)                                                      | 1.06x slower                                                                |

Benchmark hidden because not significant (3): async_tree_memoization, async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 72.1 ms: 1.09x faster                                                       |
| nbody          | 88.3 ms                                                    | 81.1 ms: 1.09x faster                                                       |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                      | 1.07x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                    | 3.65 ms: 1.01x faster                                                       |
| regex_dna      | 221 ms                                                     | 221 ms: 1.00x faster                                                        |
| regex_compile  | 137 ms                                                     | 138 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                      | 1.00x slower                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 77.4 ms: 1.13x faster                                                       |
| xml_etree_process    | 61.2 ms                                                    | 54.2 ms: 1.13x faster                                                       |
| tomli_loads          | 2.12 sec                                                   | 1.92 sec: 1.10x faster                                                      |
| xml_etree_parse      | 162 ms                                                     | 150 ms: 1.08x faster                                                        |
| json_loads           | 28.9 us                                                    | 27.0 us: 1.07x faster                                                       |
| json_dumps           | 10.7 ms                                                    | 10.2 ms: 1.05x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                     | 104 ms: 1.03x faster                                                        |
| unpickle             | 15.1 us                                                    | 14.8 us: 1.02x faster                                                       |
| unpickle_pure_python | 218 us                                                     | 214 us: 1.02x faster                                                        |
| pickle_list          | 5.11 us                                                    | 5.09 us: 1.00x faster                                                       |
| pickle               | 11.5 us                                                    | 11.5 us: 1.01x slower                                                       |
| pickle_dict          | 34.8 us                                                    | 35.1 us: 1.01x slower                                                       |
| unpickle_list        | 5.34 us                                                    | 5.41 us: 1.01x slower                                                       |
| Geometric mean       | (ref)                                                      | 1.04x faster                                                                |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                       |
| python_startup_no_site | 7.11 ms                                                    | 7.09 ms: 1.00x faster                                                       |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 10.0 ms: 1.12x faster                                                       |
| django_template | 34.8 ms                                                    | 35.7 ms: 1.03x slower                                                       |
| genshi_text     | 23.7 ms                                                    | 26.0 ms: 1.10x slower                                                       |
| genshi_xml      | 51.6 ms                                                    | 58.8 ms: 1.14x slower                                                       |
| Geometric mean  | (ref)                                                      | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.9 us: 1.48x faster                                                       |
| deepcopy                   | 367 us                                                     | 250 us: 1.47x faster                                                        |
| richards                   | 50.9 ms                                                    | 39.5 ms: 1.29x faster                                                       |
| scimark_fft                | 392 ms                                                     | 308 ms: 1.27x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                    | 2.65 us: 1.26x faster                                                       |
| richards_super             | 57.4 ms                                                    | 45.6 ms: 1.26x faster                                                       |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.42 ms: 1.19x faster                                                       |
| spectral_norm              | 116 ms                                                     | 98.6 ms: 1.18x faster                                                       |
| crypto_pyaes               | 77.5 ms                                                    | 66.5 ms: 1.16x faster                                                       |
| go                         | 145 ms                                                     | 126 ms: 1.15x faster                                                        |
| xml_etree_generate         | 87.4 ms                                                    | 77.4 ms: 1.13x faster                                                       |
| xml_etree_process          | 61.2 ms                                                    | 54.2 ms: 1.13x faster                                                       |
| mako                       | 11.2 ms                                                    | 10.0 ms: 1.12x faster                                                       |
| mdp                        | 2.79 sec                                                   | 2.52 sec: 1.11x faster                                                      |
| scimark_monte_carlo        | 69.2 ms                                                    | 62.6 ms: 1.11x faster                                                       |
| tomli_loads                | 2.12 sec                                                   | 1.92 sec: 1.10x faster                                                      |
| scimark_lu                 | 122 ms                                                     | 111 ms: 1.10x faster                                                        |
| pathlib                    | 17.3 ms                                                    | 15.8 ms: 1.10x faster                                                       |
| float                      | 78.9 ms                                                    | 72.1 ms: 1.09x faster                                                       |
| nbody                      | 88.3 ms                                                    | 81.1 ms: 1.09x faster                                                       |
| scimark_sor                | 127 ms                                                     | 117 ms: 1.09x faster                                                        |
| sqlite_synth               | 2.99 us                                                    | 2.76 us: 1.08x faster                                                       |
| coverage                   | 93.1 ms                                                    | 85.9 ms: 1.08x faster                                                       |
| xml_etree_parse            | 162 ms                                                     | 150 ms: 1.08x faster                                                        |
| pyflate                    | 484 ms                                                     | 452 ms: 1.07x faster                                                        |
| json_loads                 | 28.9 us                                                    | 27.0 us: 1.07x faster                                                       |
| fannkuch                   | 402 ms                                                     | 377 ms: 1.07x faster                                                        |
| bpe_tokeniser              | 5.02 sec                                                   | 4.71 sec: 1.07x faster                                                      |
| json                       | 5.31 ms                                                    | 4.99 ms: 1.06x faster                                                       |
| pprint_pformat             | 1.56 sec                                                   | 1.46 sec: 1.06x faster                                                      |
| json_dumps                 | 10.7 ms                                                    | 10.2 ms: 1.05x faster                                                       |
| async_tree_none            | 378 ms                                                     | 360 ms: 1.05x faster                                                        |
| pprint_safe_repr           | 758 ms                                                     | 725 ms: 1.05x faster                                                        |
| logging_format             | 6.47 us                                                    | 6.20 us: 1.04x faster                                                       |
| telco                      | 8.41 ms                                                    | 8.07 ms: 1.04x faster                                                       |
| chaos                      | 61.3 ms                                                    | 58.9 ms: 1.04x faster                                                       |
| thrift                     | 823 us                                                     | 791 us: 1.04x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                     | 104 ms: 1.03x faster                                                        |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                                        |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.03x faster                                                        |
| create_gc_cycles           | 1.82 ms                                                    | 1.77 ms: 1.02x faster                                                       |
| unpickle                   | 15.1 us                                                    | 14.8 us: 1.02x faster                                                       |
| asyncio_websockets         | 567 ms                                                     | 556 ms: 1.02x faster                                                        |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                      |
| logging_simple             | 5.74 us                                                    | 5.64 us: 1.02x faster                                                       |
| unpickle_pure_python       | 218 us                                                     | 214 us: 1.02x faster                                                        |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                       |
| deltablue                  | 3.25 ms                                                    | 3.21 ms: 1.01x faster                                                       |
| html5lib                   | 67.2 ms                                                    | 66.5 ms: 1.01x faster                                                       |
| asyncio_tcp                | 508 ms                                                     | 505 ms: 1.01x faster                                                        |
| regex_effbot               | 3.67 ms                                                    | 3.65 ms: 1.01x faster                                                       |
| pickle_list                | 5.11 us                                                    | 5.09 us: 1.00x faster                                                       |
| python_startup_no_site     | 7.11 ms                                                    | 7.09 ms: 1.00x faster                                                       |
| regex_dna                  | 221 ms                                                     | 221 ms: 1.00x faster                                                        |
| bench_thread_pool          | 834 us                                                     | 837 us: 1.00x slower                                                        |
| comprehensions             | 16.6 us                                                    | 16.7 us: 1.00x slower                                                       |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                       |
| pickle                     | 11.5 us                                                    | 11.5 us: 1.01x slower                                                       |
| regex_compile              | 137 ms                                                     | 138 ms: 1.01x slower                                                        |
| dulwich_log                | 67.2 ms                                                    | 67.6 ms: 1.01x slower                                                       |
| logging_silent             | 105 ns                                                     | 105 ns: 1.01x slower                                                        |
| pickle_dict                | 34.8 us                                                    | 35.1 us: 1.01x slower                                                       |
| sqlglot_normalize          | 110 ms                                                     | 111 ms: 1.01x slower                                                        |
| unpickle_list              | 5.34 us                                                    | 5.41 us: 1.01x slower                                                       |
| gc_traversal               | 3.98 ms                                                    | 4.04 ms: 1.02x slower                                                       |
| sqlglot_parse              | 1.32 ms                                                    | 1.35 ms: 1.02x slower                                                       |
| django_template            | 34.8 ms                                                    | 35.7 ms: 1.03x slower                                                       |
| sqlglot_optimize           | 55.5 ms                                                    | 57.1 ms: 1.03x slower                                                       |
| 2to3                       | 274 ms                                                     | 282 ms: 1.03x slower                                                        |
| async_generators           | 442 ms                                                     | 457 ms: 1.03x slower                                                        |
| raytrace                   | 267 ms                                                     | 277 ms: 1.04x slower                                                        |
| nqueens                    | 81.4 ms                                                    | 84.6 ms: 1.04x slower                                                       |
| pycparser                  | 1.16 sec                                                   | 1.21 sec: 1.05x slower                                                      |
| sympy_str                  | 282 ms                                                     | 296 ms: 1.05x slower                                                        |
| sqlglot_transpile          | 1.63 ms                                                    | 1.73 ms: 1.06x slower                                                       |
| sympy_expand               | 473 ms                                                     | 503 ms: 1.06x slower                                                        |
| hexiom                     | 6.30 ms                                                    | 6.83 ms: 1.09x slower                                                       |
| async_tree_io_tg           | 936 ms                                                     | 1.02 sec: 1.09x slower                                                      |
| genshi_text                | 23.7 ms                                                    | 26.0 ms: 1.10x slower                                                       |
| sympy_sum                  | 156 ms                                                     | 171 ms: 1.10x slower                                                        |
| generators                 | 29.6 ms                                                    | 32.6 ms: 1.10x slower                                                       |
| sympy_integrate            | 20.5 ms                                                    | 22.7 ms: 1.11x slower                                                       |
| docutils                   | 2.83 sec                                                   | 3.20 sec: 1.13x slower                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 666 ms: 1.13x slower                                                        |
| genshi_xml                 | 51.6 ms                                                    | 58.8 ms: 1.14x slower                                                       |
| async_tree_memoization_tg  | 444 ms                                                     | 513 ms: 1.16x slower                                                        |
| async_tree_none_tg         | 336 ms                                                     | 401 ms: 1.19x slower                                                        |
| Geometric mean             | (ref)                                                      | 1.03x faster                                                                |

Benchmark hidden because not significant (9): async_tree_memoization, pylint, async_tree_cpu_io_mixed, typing_runtime_protocols, pickle_pure_python, coroutines, regex_v8, async_tree_io, tornado_http
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240918-3.14.0a0-f2327f4-JIT/bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4.json: unpack_sequence

# HPT report

- Reliability score: 92.50% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x