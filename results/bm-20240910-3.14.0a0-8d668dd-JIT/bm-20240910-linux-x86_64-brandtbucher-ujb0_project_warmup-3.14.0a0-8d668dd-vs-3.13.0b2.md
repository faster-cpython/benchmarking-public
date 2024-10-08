# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: ujb0_project_warmup
- machine: linux-x86_64
- commit hash: 8d668dd
- commit date: 2024-09-10
- overall geometric mean: 1.00x faster
- HPT reliability: 67.47%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 289 ms: 1.05x slower                                                       |
| docutils       | 2.83 sec                                                   | 3.48 sec: 1.23x slower                                                     |
| html5lib       | 67.2 ms                                                    | 74.4 ms: 1.11x slower                                                      |
| tornado_http   | 94.6 ms                                                    | 114 ms: 1.21x slower                                                       |
| Geometric mean | (ref)                                                      | 1.15x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 338 ms: 1.12x faster                                                       |
| async_tree_memoization     | 463 ms                                                     | 423 ms: 1.10x faster                                                       |
| async_tree_memoization_tg  | 444 ms                                                     | 411 ms: 1.08x faster                                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 547 ms: 1.07x faster                                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 571 ms: 1.07x faster                                                       |
| async_tree_none_tg         | 336 ms                                                     | 316 ms: 1.07x faster                                                       |
| Geometric mean             | (ref)                                                      | 1.06x faster                                                               |

Benchmark hidden because not significant (2): async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 68.4 ms: 1.15x faster                                                      |
| nbody          | 88.3 ms                                                    | 79.8 ms: 1.11x faster                                                      |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                      | 1.09x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 219 ms: 1.01x faster                                                       |
| regex_effbot   | 3.67 ms                                                    | 3.72 ms: 1.01x slower                                                      |
| regex_v8       | 25.1 ms                                                    | 25.8 ms: 1.03x slower                                                      |
| regex_compile  | 137 ms                                                     | 151 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                      | 1.03x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_process    | 61.2 ms                                                    | 54.4 ms: 1.12x faster                                                      |
| xml_etree_parse      | 162 ms                                                     | 146 ms: 1.11x faster                                                       |
| xml_etree_generate   | 87.4 ms                                                    | 78.7 ms: 1.11x faster                                                      |
| unpickle_pure_python | 218 us                                                     | 196 us: 1.11x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                     | 98.0 ms: 1.10x faster                                                      |
| json_dumps           | 10.7 ms                                                    | 9.95 ms: 1.08x faster                                                      |
| unpickle_list        | 5.34 us                                                    | 5.23 us: 1.02x faster                                                      |
| pickle_dict          | 34.8 us                                                    | 34.2 us: 1.02x faster                                                      |
| unpickle             | 15.1 us                                                    | 14.9 us: 1.01x faster                                                      |
| pickle               | 11.5 us                                                    | 11.6 us: 1.01x slower                                                      |
| pickle_list          | 5.11 us                                                    | 5.17 us: 1.01x slower                                                      |
| json_loads           | 28.9 us                                                    | 29.7 us: 1.03x slower                                                      |
| pickle_pure_python   | 305 us                                                     | 319 us: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                      | 1.04x faster                                                               |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.7 ms: 1.01x faster                                                      |
| python_startup_no_site | 7.11 ms                                                    | 7.15 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                      | 1.00x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|-----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.86 ms: 1.14x faster                                                      |
| genshi_text     | 23.7 ms                                                    | 23.1 ms: 1.03x faster                                                      |
| django_template | 34.8 ms                                                    | 40.4 ms: 1.16x slower                                                      |
| genshi_xml      | 51.6 ms                                                    | 62.3 ms: 1.21x slower                                                      |
| Geometric mean  | (ref)                                                      | 1.05x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 27.3 us: 1.46x faster                                                      |
| deepcopy                   | 367 us                                                     | 280 us: 1.31x faster                                                       |
| scimark_fft                | 392 ms                                                     | 310 ms: 1.27x faster                                                       |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.27 ms: 1.24x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                    | 2.74 us: 1.22x faster                                                      |
| scimark_monte_carlo        | 69.2 ms                                                    | 58.8 ms: 1.18x faster                                                      |
| float                      | 78.9 ms                                                    | 68.4 ms: 1.15x faster                                                      |
| crypto_pyaes               | 77.5 ms                                                    | 67.2 ms: 1.15x faster                                                      |
| mako                       | 11.2 ms                                                    | 9.86 ms: 1.14x faster                                                      |
| spectral_norm              | 116 ms                                                     | 103 ms: 1.13x faster                                                       |
| xml_etree_process          | 61.2 ms                                                    | 54.4 ms: 1.12x faster                                                      |
| gc_traversal               | 3.98 ms                                                    | 3.55 ms: 1.12x faster                                                      |
| async_tree_none            | 378 ms                                                     | 338 ms: 1.12x faster                                                       |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.11x faster                                                       |
| xml_etree_generate         | 87.4 ms                                                    | 78.7 ms: 1.11x faster                                                      |
| unpickle_pure_python       | 218 us                                                     | 196 us: 1.11x faster                                                       |
| pyflate                    | 484 ms                                                     | 436 ms: 1.11x faster                                                       |
| nbody                      | 88.3 ms                                                    | 79.8 ms: 1.11x faster                                                      |
| scimark_lu                 | 122 ms                                                     | 110 ms: 1.11x faster                                                       |
| bpe_tokeniser              | 5.02 sec                                                   | 4.55 sec: 1.10x faster                                                     |
| telco                      | 8.41 ms                                                    | 7.62 ms: 1.10x faster                                                      |
| pathlib                    | 17.3 ms                                                    | 15.8 ms: 1.10x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                     | 98.0 ms: 1.10x faster                                                      |
| async_tree_memoization     | 463 ms                                                     | 423 ms: 1.10x faster                                                       |
| async_tree_memoization_tg  | 444 ms                                                     | 411 ms: 1.08x faster                                                       |
| json_dumps                 | 10.7 ms                                                    | 9.95 ms: 1.08x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 547 ms: 1.07x faster                                                       |
| coverage                   | 93.1 ms                                                    | 86.8 ms: 1.07x faster                                                      |
| scimark_sor                | 127 ms                                                     | 119 ms: 1.07x faster                                                       |
| sqlite_synth               | 2.99 us                                                    | 2.79 us: 1.07x faster                                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 571 ms: 1.07x faster                                                       |
| fannkuch                   | 402 ms                                                     | 376 ms: 1.07x faster                                                       |
| async_tree_none_tg         | 336 ms                                                     | 316 ms: 1.07x faster                                                       |
| richards                   | 50.9 ms                                                    | 48.3 ms: 1.05x faster                                                      |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                       |
| richards_super             | 57.4 ms                                                    | 55.8 ms: 1.03x faster                                                      |
| logging_silent             | 105 ns                                                     | 102 ns: 1.03x faster                                                       |
| genshi_text                | 23.7 ms                                                    | 23.1 ms: 1.03x faster                                                      |
| mdp                        | 2.79 sec                                                   | 2.72 sec: 1.03x faster                                                     |
| typing_runtime_protocols   | 165 us                                                     | 161 us: 1.02x faster                                                       |
| chaos                      | 61.3 ms                                                    | 59.9 ms: 1.02x faster                                                      |
| create_gc_cycles           | 1.82 ms                                                    | 1.78 ms: 1.02x faster                                                      |
| unpickle_list              | 5.34 us                                                    | 5.23 us: 1.02x faster                                                      |
| pickle_dict                | 34.8 us                                                    | 34.2 us: 1.02x faster                                                      |
| thrift                     | 823 us                                                     | 809 us: 1.02x faster                                                       |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                                       |
| unpickle                   | 15.1 us                                                    | 14.9 us: 1.01x faster                                                      |
| regex_dna                  | 221 ms                                                     | 219 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.82 sec: 1.01x faster                                                     |
| json                       | 5.31 ms                                                    | 5.25 ms: 1.01x faster                                                      |
| python_startup             | 10.8 ms                                                    | 10.7 ms: 1.01x faster                                                      |
| meteor_contest             | 110 ms                                                     | 109 ms: 1.01x faster                                                       |
| python_startup_no_site     | 7.11 ms                                                    | 7.15 ms: 1.01x slower                                                      |
| comprehensions             | 16.6 us                                                    | 16.7 us: 1.01x slower                                                      |
| logging_format             | 6.47 us                                                    | 6.53 us: 1.01x slower                                                      |
| pickle                     | 11.5 us                                                    | 11.6 us: 1.01x slower                                                      |
| pickle_list                | 5.11 us                                                    | 5.17 us: 1.01x slower                                                      |
| regex_effbot               | 3.67 ms                                                    | 3.72 ms: 1.01x slower                                                      |
| logging_simple             | 5.74 us                                                    | 5.83 us: 1.02x slower                                                      |
| bench_mp_pool              | 23.9 ms                                                    | 24.4 ms: 1.02x slower                                                      |
| pprint_safe_repr           | 758 ms                                                     | 776 ms: 1.02x slower                                                       |
| nqueens                    | 81.4 ms                                                    | 83.3 ms: 1.02x slower                                                      |
| regex_v8                   | 25.1 ms                                                    | 25.8 ms: 1.03x slower                                                      |
| json_loads                 | 28.9 us                                                    | 29.7 us: 1.03x slower                                                      |
| asyncio_tcp                | 508 ms                                                     | 525 ms: 1.03x slower                                                       |
| async_generators           | 442 ms                                                     | 457 ms: 1.03x slower                                                       |
| coroutines                 | 23.2 ms                                                    | 24.1 ms: 1.04x slower                                                      |
| pickle_pure_python         | 305 us                                                     | 319 us: 1.04x slower                                                       |
| raytrace                   | 267 ms                                                     | 281 ms: 1.05x slower                                                       |
| 2to3                       | 274 ms                                                     | 289 ms: 1.05x slower                                                       |
| pprint_pformat             | 1.56 sec                                                   | 1.66 sec: 1.07x slower                                                     |
| bench_thread_pool          | 834 us                                                     | 892 us: 1.07x slower                                                       |
| deltablue                  | 3.25 ms                                                    | 3.59 ms: 1.10x slower                                                      |
| regex_compile              | 137 ms                                                     | 151 ms: 1.11x slower                                                       |
| html5lib                   | 67.2 ms                                                    | 74.4 ms: 1.11x slower                                                      |
| sqlglot_normalize          | 110 ms                                                     | 126 ms: 1.15x slower                                                       |
| sqlglot_optimize           | 55.5 ms                                                    | 64.0 ms: 1.15x slower                                                      |
| django_template            | 34.8 ms                                                    | 40.4 ms: 1.16x slower                                                      |
| pycparser                  | 1.16 sec                                                   | 1.35 sec: 1.16x slower                                                     |
| sympy_expand               | 473 ms                                                     | 554 ms: 1.17x slower                                                       |
| generators                 | 29.6 ms                                                    | 34.7 ms: 1.17x slower                                                      |
| sympy_str                  | 282 ms                                                     | 336 ms: 1.19x slower                                                       |
| hexiom                     | 6.30 ms                                                    | 7.49 ms: 1.19x slower                                                      |
| tornado_http               | 94.6 ms                                                    | 114 ms: 1.21x slower                                                       |
| genshi_xml                 | 51.6 ms                                                    | 62.3 ms: 1.21x slower                                                      |
| go                         | 145 ms                                                     | 176 ms: 1.22x slower                                                       |
| docutils                   | 2.83 sec                                                   | 3.48 sec: 1.23x slower                                                     |
| sympy_integrate            | 20.5 ms                                                    | 25.3 ms: 1.23x slower                                                      |
| sqlglot_parse              | 1.32 ms                                                    | 1.68 ms: 1.27x slower                                                      |
| sqlglot_transpile          | 1.63 ms                                                    | 2.08 ms: 1.28x slower                                                      |
| sympy_sum                  | 156 ms                                                     | 209 ms: 1.34x slower                                                       |
| pylint                     | 317 ms                                                     | 454 ms: 1.43x slower                                                       |
| Geometric mean             | (ref)                                                      | 1.00x faster                                                               |

Benchmark hidden because not significant (3): async_tree_io_tg, tomli_loads, async_tree_io
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240910-3.14.0a0-8d668dd-JIT/bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd.json: unpack_sequence

# HPT report

- Reliability score: 67.47% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.16x