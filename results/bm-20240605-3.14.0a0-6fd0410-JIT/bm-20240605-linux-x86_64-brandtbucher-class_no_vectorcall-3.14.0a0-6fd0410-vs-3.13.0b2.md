# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: class_no_vectorcall
- machine: linux-x86_64
- commit hash: 6fd0410
- commit date: 2024-06-05
- overall geometric mean: 1.01x faster
- HPT reliability: 85.70%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-6fd0410 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 279 ms: 1.02x slower                                                       |
| docutils       | 2.83 sec                                                   | 2.96 sec: 1.05x slower                                                     |
| html5lib       | 67.2 ms                                                    | 67.8 ms: 1.01x slower                                                      |
| tornado_http   | 94.6 ms                                                    | 97.8 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                      | 1.03x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-6fd0410 |
|-------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 611 ms                                                     | 632 ms: 1.03x slower                                                       |
| Geometric mean          | (ref)                                                      | 1.01x slower                                                               |

Benchmark hidden because not significant (7): async_tree_memoization_tg, async_tree_io_tg, async_tree_none, async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-6fd0410 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 80.6 ms: 1.10x faster                                                      |
| float          | 78.9 ms                                                    | 72.5 ms: 1.09x faster                                                      |
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                      | 1.07x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-6fd0410 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 138 ms: 1.01x slower                                                       |
| regex_dna      | 221 ms                                                     | 229 ms: 1.04x slower                                                       |
| regex_effbot   | 3.67 ms                                                    | 3.81 ms: 1.04x slower                                                      |
| regex_v8       | 25.1 ms                                                    | 26.1 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                      | 1.03x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-6fd0410 |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 149 ms: 1.09x faster                                                       |
| tomli_loads          | 2.12 sec                                                   | 1.96 sec: 1.08x faster                                                     |
| xml_etree_generate   | 87.4 ms                                                    | 81.1 ms: 1.08x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                     | 101 ms: 1.07x faster                                                       |
| xml_etree_process    | 61.2 ms                                                    | 57.7 ms: 1.06x faster                                                      |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                      |
| pickle_pure_python   | 305 us                                                     | 297 us: 1.03x faster                                                       |
| unpickle_pure_python | 218 us                                                     | 220 us: 1.01x slower                                                       |
| unpickle_list        | 5.34 us                                                    | 5.46 us: 1.02x slower                                                      |
| pickle_dict          | 34.8 us                                                    | 35.9 us: 1.03x slower                                                      |
| pickle_list          | 5.11 us                                                    | 5.29 us: 1.04x slower                                                      |
| pickle               | 11.5 us                                                    | 11.9 us: 1.04x slower                                                      |
| unpickle             | 15.1 us                                                    | 15.9 us: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-6fd0410 |
|------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 11.2 ms: 1.04x slower                                                      |
| python_startup_no_site | 7.11 ms                                                    | 7.61 ms: 1.07x slower                                                      |
| Geometric mean         | (ref)                                                      | 1.05x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-6fd0410 |
|-----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.98 ms: 1.13x faster                                                      |
| genshi_text     | 23.7 ms                                                    | 24.8 ms: 1.05x slower                                                      |
| django_template | 34.8 ms                                                    | 36.8 ms: 1.06x slower                                                      |
| genshi_xml      | 51.6 ms                                                    | 57.0 ms: 1.10x slower                                                      |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                               |

All benchmarks:
===============

| Benchmark               | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-6fd0410 |
|-------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| scimark_fft             | 392 ms                                                     | 318 ms: 1.23x faster                                                       |
| richards                | 50.9 ms                                                    | 41.5 ms: 1.23x faster                                                      |
| richards_super          | 57.4 ms                                                    | 47.9 ms: 1.20x faster                                                      |
| scimark_sparse_mat_mult | 5.27 ms                                                    | 4.43 ms: 1.19x faster                                                      |
| spectral_norm           | 116 ms                                                     | 102 ms: 1.14x faster                                                       |
| crypto_pyaes            | 77.5 ms                                                    | 68.4 ms: 1.13x faster                                                      |
| mako                    | 11.2 ms                                                    | 9.98 ms: 1.13x faster                                                      |
| fannkuch                | 402 ms                                                     | 361 ms: 1.11x faster                                                       |
| scimark_monte_carlo     | 69.2 ms                                                    | 63.0 ms: 1.10x faster                                                      |
| nbody                   | 88.3 ms                                                    | 80.6 ms: 1.10x faster                                                      |
| float                   | 78.9 ms                                                    | 72.5 ms: 1.09x faster                                                      |
| xml_etree_parse         | 162 ms                                                     | 149 ms: 1.09x faster                                                       |
| gc_traversal            | 3.98 ms                                                    | 3.66 ms: 1.09x faster                                                      |
| tomli_loads             | 2.12 sec                                                   | 1.96 sec: 1.08x faster                                                     |
| xml_etree_generate      | 87.4 ms                                                    | 81.1 ms: 1.08x faster                                                      |
| xml_etree_iterparse     | 107 ms                                                     | 101 ms: 1.07x faster                                                       |
| pyflate                 | 484 ms                                                     | 454 ms: 1.07x faster                                                       |
| xml_etree_process       | 61.2 ms                                                    | 57.7 ms: 1.06x faster                                                      |
| pathlib                 | 17.3 ms                                                    | 16.4 ms: 1.06x faster                                                      |
| pprint_pformat          | 1.56 sec                                                   | 1.48 sec: 1.05x faster                                                     |
| pprint_safe_repr        | 758 ms                                                     | 723 ms: 1.05x faster                                                       |
| sqlite_synth            | 2.99 us                                                    | 2.86 us: 1.05x faster                                                      |
| telco                   | 8.41 ms                                                    | 8.04 ms: 1.05x faster                                                      |
| json_dumps              | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                      |
| deepcopy_memo           | 39.7 us                                                    | 38.1 us: 1.04x faster                                                      |
| logging_format          | 6.47 us                                                    | 6.29 us: 1.03x faster                                                      |
| pickle_pure_python      | 305 us                                                     | 297 us: 1.03x faster                                                       |
| deepcopy_reduce         | 3.35 us                                                    | 3.27 us: 1.02x faster                                                      |
| logging_simple          | 5.74 us                                                    | 5.61 us: 1.02x faster                                                      |
| chaos                   | 61.3 ms                                                    | 60.3 ms: 1.02x faster                                                      |
| pidigits                | 191 ms                                                     | 188 ms: 1.02x faster                                                       |
| create_gc_cycles        | 1.82 ms                                                    | 1.79 ms: 1.02x faster                                                      |
| meteor_contest          | 110 ms                                                     | 108 ms: 1.01x faster                                                       |
| sqlglot_parse           | 1.32 ms                                                    | 1.31 ms: 1.01x faster                                                      |
| mdp                     | 2.79 sec                                                   | 2.77 sec: 1.01x faster                                                     |
| coroutines              | 23.2 ms                                                    | 23.1 ms: 1.01x faster                                                      |
| sqlglot_transpile       | 1.63 ms                                                    | 1.64 ms: 1.00x slower                                                      |
| regex_compile           | 137 ms                                                     | 138 ms: 1.01x slower                                                       |
| bench_mp_pool           | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                      |
| comprehensions          | 16.6 us                                                    | 16.7 us: 1.01x slower                                                      |
| unpickle_pure_python    | 218 us                                                     | 220 us: 1.01x slower                                                       |
| html5lib                | 67.2 ms                                                    | 67.8 ms: 1.01x slower                                                      |
| asyncio_tcp_ssl         | 1.84 sec                                                   | 1.86 sec: 1.01x slower                                                     |
| coverage                | 93.1 ms                                                    | 94.2 ms: 1.01x slower                                                      |
| logging_silent          | 105 ns                                                     | 106 ns: 1.01x slower                                                       |
| 2to3                    | 274 ms                                                     | 279 ms: 1.02x slower                                                       |
| go                      | 145 ms                                                     | 147 ms: 1.02x slower                                                       |
| deepcopy                | 367 us                                                     | 374 us: 1.02x slower                                                       |
| sqlglot_optimize        | 55.5 ms                                                    | 56.6 ms: 1.02x slower                                                      |
| scimark_lu              | 122 ms                                                     | 124 ms: 1.02x slower                                                       |
| unpickle_list           | 5.34 us                                                    | 5.46 us: 1.02x slower                                                      |
| json                    | 5.31 ms                                                    | 5.43 ms: 1.02x slower                                                      |
| dask                    | 369 ms                                                     | 379 ms: 1.02x slower                                                       |
| asyncio_tcp             | 508 ms                                                     | 521 ms: 1.03x slower                                                       |
| sqlglot_normalize       | 110 ms                                                     | 113 ms: 1.03x slower                                                       |
| pickle_dict             | 34.8 us                                                    | 35.9 us: 1.03x slower                                                      |
| tornado_http            | 94.6 ms                                                    | 97.8 ms: 1.03x slower                                                      |
| async_tree_cpu_io_mixed | 611 ms                                                     | 632 ms: 1.03x slower                                                       |
| generators              | 29.6 ms                                                    | 30.7 ms: 1.04x slower                                                      |
| regex_dna               | 221 ms                                                     | 229 ms: 1.04x slower                                                       |
| pickle_list             | 5.11 us                                                    | 5.29 us: 1.04x slower                                                      |
| pickle                  | 11.5 us                                                    | 11.9 us: 1.04x slower                                                      |
| dulwich_log             | 67.2 ms                                                    | 69.7 ms: 1.04x slower                                                      |
| python_startup          | 10.8 ms                                                    | 11.2 ms: 1.04x slower                                                      |
| regex_effbot            | 3.67 ms                                                    | 3.81 ms: 1.04x slower                                                      |
| regex_v8                | 25.1 ms                                                    | 26.1 ms: 1.04x slower                                                      |
| pycparser               | 1.16 sec                                                   | 1.21 sec: 1.04x slower                                                     |
| raytrace                | 267 ms                                                     | 279 ms: 1.05x slower                                                       |
| docutils                | 2.83 sec                                                   | 2.96 sec: 1.05x slower                                                     |
| hexiom                  | 6.30 ms                                                    | 6.59 ms: 1.05x slower                                                      |
| async_generators        | 442 ms                                                     | 464 ms: 1.05x slower                                                       |
| genshi_text             | 23.7 ms                                                    | 24.8 ms: 1.05x slower                                                      |
| bench_thread_pool       | 834 us                                                     | 877 us: 1.05x slower                                                       |
| unpickle                | 15.1 us                                                    | 15.9 us: 1.05x slower                                                      |
| nqueens                 | 81.4 ms                                                    | 85.7 ms: 1.05x slower                                                      |
| django_template         | 34.8 ms                                                    | 36.8 ms: 1.06x slower                                                      |
| sympy_str               | 282 ms                                                     | 300 ms: 1.06x slower                                                       |
| sympy_expand            | 473 ms                                                     | 506 ms: 1.07x slower                                                       |
| python_startup_no_site  | 7.11 ms                                                    | 7.61 ms: 1.07x slower                                                      |
| sympy_integrate         | 20.5 ms                                                    | 22.5 ms: 1.10x slower                                                      |
| sympy_sum               | 156 ms                                                     | 172 ms: 1.10x slower                                                       |
| genshi_xml              | 51.6 ms                                                    | 57.0 ms: 1.10x slower                                                      |
| pylint                  | 317 ms                                                     | 353 ms: 1.11x slower                                                       |
| deltablue               | 3.25 ms                                                    | 3.73 ms: 1.15x slower                                                      |
| Geometric mean          | (ref)                                                      | 1.01x faster                                                               |

Benchmark hidden because not significant (12): async_tree_memoization_tg, async_tree_io_tg, thrift, async_tree_none, asyncio_websockets, typing_runtime_protocols, scimark_sor, json_loads, async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_io
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, chameleon, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 85.70% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x