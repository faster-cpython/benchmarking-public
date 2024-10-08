# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: ujb0_project_warmup
- machine: linux-x86_64
- commit hash: f67fedc
- commit date: 2024-09-09
- overall geometric mean: 1.00x slower
- HPT reliability: 54.87%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 292 ms: 1.06x slower                                                       |
| docutils       | 2.83 sec                                                   | 3.47 sec: 1.23x slower                                                     |
| html5lib       | 67.2 ms                                                    | 70.6 ms: 1.05x slower                                                      |
| tornado_http   | 94.6 ms                                                    | 119 ms: 1.26x slower                                                       |
| Geometric mean | (ref)                                                      | 1.15x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 339 ms: 1.12x faster                                                       |
| async_tree_memoization     | 463 ms                                                     | 422 ms: 1.10x faster                                                       |
| async_tree_memoization_tg  | 444 ms                                                     | 409 ms: 1.08x faster                                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 571 ms: 1.07x faster                                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 550 ms: 1.07x faster                                                       |
| async_tree_none_tg         | 336 ms                                                     | 318 ms: 1.06x faster                                                       |
| Geometric mean             | (ref)                                                      | 1.06x faster                                                               |

Benchmark hidden because not significant (2): async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 69.9 ms: 1.13x faster                                                      |
| nbody          | 88.3 ms                                                    | 82.2 ms: 1.07x faster                                                      |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                      | 1.08x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 215 ms: 1.03x faster                                                       |
| regex_effbot   | 3.67 ms                                                    | 3.77 ms: 1.03x slower                                                      |
| regex_v8       | 25.1 ms                                                    | 25.9 ms: 1.03x slower                                                      |
| regex_compile  | 137 ms                                                     | 155 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                      | 1.04x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 218 us                                                     | 191 us: 1.14x faster                                                       |
| xml_etree_process    | 61.2 ms                                                    | 54.0 ms: 1.13x faster                                                      |
| xml_etree_parse      | 162 ms                                                     | 144 ms: 1.12x faster                                                       |
| xml_etree_generate   | 87.4 ms                                                    | 78.1 ms: 1.12x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                     | 98.2 ms: 1.09x faster                                                      |
| json_dumps           | 10.7 ms                                                    | 9.90 ms: 1.08x faster                                                      |
| unpickle             | 15.1 us                                                    | 14.7 us: 1.03x faster                                                      |
| tomli_loads          | 2.12 sec                                                   | 2.06 sec: 1.03x faster                                                     |
| pickle               | 11.5 us                                                    | 11.4 us: 1.01x faster                                                      |
| unpickle_list        | 5.34 us                                                    | 5.31 us: 1.01x faster                                                      |
| pickle_dict          | 34.8 us                                                    | 35.2 us: 1.01x slower                                                      |
| pickle_list          | 5.11 us                                                    | 5.19 us: 1.02x slower                                                      |
| json_loads           | 28.9 us                                                    | 29.5 us: 1.02x slower                                                      |
| pickle_pure_python   | 305 us                                                     | 314 us: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                      | 1.05x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.8 ms: 1.00x slower                                                      |
| python_startup_no_site | 7.11 ms                                                    | 7.19 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                      | 1.01x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|-----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.65 ms: 1.16x faster                                                      |
| genshi_text     | 23.7 ms                                                    | 22.6 ms: 1.04x faster                                                      |
| django_template | 34.8 ms                                                    | 38.8 ms: 1.12x slower                                                      |
| genshi_xml      | 51.6 ms                                                    | 59.0 ms: 1.14x slower                                                      |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 27.1 us: 1.47x faster                                                      |
| deepcopy                   | 367 us                                                     | 267 us: 1.38x faster                                                       |
| scimark_fft                | 392 ms                                                     | 312 ms: 1.26x faster                                                       |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.38 ms: 1.20x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                    | 2.79 us: 1.20x faster                                                      |
| scimark_monte_carlo        | 69.2 ms                                                    | 58.1 ms: 1.19x faster                                                      |
| mako                       | 11.2 ms                                                    | 9.65 ms: 1.16x faster                                                      |
| unpickle_pure_python       | 218 us                                                     | 191 us: 1.14x faster                                                       |
| crypto_pyaes               | 77.5 ms                                                    | 68.2 ms: 1.14x faster                                                      |
| xml_etree_process          | 61.2 ms                                                    | 54.0 ms: 1.13x faster                                                      |
| float                      | 78.9 ms                                                    | 69.9 ms: 1.13x faster                                                      |
| xml_etree_parse            | 162 ms                                                     | 144 ms: 1.12x faster                                                       |
| xml_etree_generate         | 87.4 ms                                                    | 78.1 ms: 1.12x faster                                                      |
| async_tree_none            | 378 ms                                                     | 339 ms: 1.12x faster                                                       |
| scimark_lu                 | 122 ms                                                     | 109 ms: 1.11x faster                                                       |
| bpe_tokeniser              | 5.02 sec                                                   | 4.51 sec: 1.11x faster                                                     |
| async_tree_memoization     | 463 ms                                                     | 422 ms: 1.10x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                     | 98.2 ms: 1.09x faster                                                      |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                                      |
| coverage                   | 93.1 ms                                                    | 85.4 ms: 1.09x faster                                                      |
| telco                      | 8.41 ms                                                    | 7.75 ms: 1.09x faster                                                      |
| async_tree_memoization_tg  | 444 ms                                                     | 409 ms: 1.08x faster                                                       |
| json_dumps                 | 10.7 ms                                                    | 9.90 ms: 1.08x faster                                                      |
| fannkuch                   | 402 ms                                                     | 372 ms: 1.08x faster                                                       |
| spectral_norm              | 116 ms                                                     | 107 ms: 1.08x faster                                                       |
| sqlite_synth               | 2.99 us                                                    | 2.77 us: 1.08x faster                                                      |
| nbody                      | 88.3 ms                                                    | 82.2 ms: 1.07x faster                                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 571 ms: 1.07x faster                                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 550 ms: 1.07x faster                                                       |
| async_tree_none_tg         | 336 ms                                                     | 318 ms: 1.06x faster                                                       |
| gc_traversal               | 3.98 ms                                                    | 3.78 ms: 1.05x faster                                                      |
| scimark_sor                | 127 ms                                                     | 122 ms: 1.05x faster                                                       |
| genshi_text                | 23.7 ms                                                    | 22.6 ms: 1.04x faster                                                      |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                       |
| unpickle                   | 15.1 us                                                    | 14.7 us: 1.03x faster                                                      |
| tomli_loads                | 2.12 sec                                                   | 2.06 sec: 1.03x faster                                                     |
| regex_dna                  | 221 ms                                                     | 215 ms: 1.03x faster                                                       |
| pyflate                    | 484 ms                                                     | 471 ms: 1.03x faster                                                       |
| mdp                        | 2.79 sec                                                   | 2.72 sec: 1.03x faster                                                     |
| thrift                     | 823 us                                                     | 809 us: 1.02x faster                                                       |
| asyncio_websockets         | 567 ms                                                     | 557 ms: 1.02x faster                                                       |
| create_gc_cycles           | 1.82 ms                                                    | 1.79 ms: 1.02x faster                                                      |
| logging_silent             | 105 ns                                                     | 103 ns: 1.02x faster                                                       |
| meteor_contest             | 110 ms                                                     | 108 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.82 sec: 1.01x faster                                                     |
| pickle                     | 11.5 us                                                    | 11.4 us: 1.01x faster                                                      |
| unpickle_list              | 5.34 us                                                    | 5.31 us: 1.01x faster                                                      |
| python_startup             | 10.8 ms                                                    | 10.8 ms: 1.00x slower                                                      |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                      |
| deltablue                  | 3.25 ms                                                    | 3.29 ms: 1.01x slower                                                      |
| pickle_dict                | 34.8 us                                                    | 35.2 us: 1.01x slower                                                      |
| python_startup_no_site     | 7.11 ms                                                    | 7.19 ms: 1.01x slower                                                      |
| chaos                      | 61.3 ms                                                    | 62.3 ms: 1.02x slower                                                      |
| pickle_list                | 5.11 us                                                    | 5.19 us: 1.02x slower                                                      |
| comprehensions             | 16.6 us                                                    | 17.0 us: 1.02x slower                                                      |
| json_loads                 | 28.9 us                                                    | 29.5 us: 1.02x slower                                                      |
| logging_simple             | 5.74 us                                                    | 5.88 us: 1.02x slower                                                      |
| regex_effbot               | 3.67 ms                                                    | 3.77 ms: 1.03x slower                                                      |
| asyncio_tcp                | 508 ms                                                     | 522 ms: 1.03x slower                                                       |
| pickle_pure_python         | 305 us                                                     | 314 us: 1.03x slower                                                       |
| async_generators           | 442 ms                                                     | 455 ms: 1.03x slower                                                       |
| coroutines                 | 23.2 ms                                                    | 23.9 ms: 1.03x slower                                                      |
| nqueens                    | 81.4 ms                                                    | 84.0 ms: 1.03x slower                                                      |
| regex_v8                   | 25.1 ms                                                    | 25.9 ms: 1.03x slower                                                      |
| raytrace                   | 267 ms                                                     | 275 ms: 1.03x slower                                                       |
| html5lib                   | 67.2 ms                                                    | 70.6 ms: 1.05x slower                                                      |
| richards                   | 50.9 ms                                                    | 53.8 ms: 1.06x slower                                                      |
| richards_super             | 57.4 ms                                                    | 60.8 ms: 1.06x slower                                                      |
| 2to3                       | 274 ms                                                     | 292 ms: 1.06x slower                                                       |
| pprint_pformat             | 1.56 sec                                                   | 1.66 sec: 1.07x slower                                                     |
| bench_thread_pool          | 834 us                                                     | 898 us: 1.08x slower                                                       |
| django_template            | 34.8 ms                                                    | 38.8 ms: 1.12x slower                                                      |
| pycparser                  | 1.16 sec                                                   | 1.30 sec: 1.13x slower                                                     |
| sqlglot_normalize          | 110 ms                                                     | 125 ms: 1.13x slower                                                       |
| regex_compile              | 137 ms                                                     | 155 ms: 1.13x slower                                                       |
| hexiom                     | 6.30 ms                                                    | 7.14 ms: 1.13x slower                                                      |
| genshi_xml                 | 51.6 ms                                                    | 59.0 ms: 1.14x slower                                                      |
| generators                 | 29.6 ms                                                    | 34.8 ms: 1.17x slower                                                      |
| sympy_expand               | 473 ms                                                     | 556 ms: 1.18x slower                                                       |
| sqlglot_optimize           | 55.5 ms                                                    | 67.1 ms: 1.21x slower                                                      |
| sympy_str                  | 282 ms                                                     | 341 ms: 1.21x slower                                                       |
| docutils                   | 2.83 sec                                                   | 3.47 sec: 1.23x slower                                                     |
| go                         | 145 ms                                                     | 178 ms: 1.23x slower                                                       |
| tornado_http               | 94.6 ms                                                    | 119 ms: 1.26x slower                                                       |
| sqlglot_parse              | 1.32 ms                                                    | 1.73 ms: 1.31x slower                                                      |
| sqlglot_transpile          | 1.63 ms                                                    | 2.17 ms: 1.33x slower                                                      |
| sympy_integrate            | 20.5 ms                                                    | 27.3 ms: 1.33x slower                                                      |
| sympy_sum                  | 156 ms                                                     | 214 ms: 1.37x slower                                                       |
| pylint                     | 317 ms                                                     | 480 ms: 1.51x slower                                                       |
| Geometric mean             | (ref)                                                      | 1.00x slower                                                               |

Benchmark hidden because not significant (6): async_tree_io_tg, logging_format, typing_runtime_protocols, json, pprint_safe_repr, async_tree_io
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240909-3.14.0a0-f67fedc-JIT/bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc.json: unpack_sequence

# HPT report

- Reliability score: 54.87% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.16x