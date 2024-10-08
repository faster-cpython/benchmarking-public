# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: ujb0_project_warmup
- machine: linux-x86_64
- commit hash: c66bd3e
- commit date: 2024-09-09
- overall geometric mean: 1.00x faster
- HPT reliability: 87.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 292 ms: 1.06x slower                                                       |
| docutils       | 2.83 sec                                                   | 3.46 sec: 1.22x slower                                                     |
| html5lib       | 67.2 ms                                                    | 73.0 ms: 1.09x slower                                                      |
| tornado_http   | 94.6 ms                                                    | 119 ms: 1.25x slower                                                       |
| Geometric mean | (ref)                                                      | 1.15x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 338 ms: 1.12x faster                                                       |
| async_tree_memoization     | 463 ms                                                     | 426 ms: 1.09x faster                                                       |
| async_tree_memoization_tg  | 444 ms                                                     | 415 ms: 1.07x faster                                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 573 ms: 1.07x faster                                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 551 ms: 1.07x faster                                                       |
| async_tree_none_tg         | 336 ms                                                     | 321 ms: 1.05x faster                                                       |
| async_tree_io_tg           | 936 ms                                                     | 905 ms: 1.03x faster                                                       |
| Geometric mean             | (ref)                                                      | 1.06x faster                                                               |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 69.8 ms: 1.13x faster                                                      |
| nbody          | 88.3 ms                                                    | 83.1 ms: 1.06x faster                                                      |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                      | 1.07x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 206 ms: 1.07x faster                                                       |
| regex_effbot   | 3.67 ms                                                    | 3.45 ms: 1.07x faster                                                      |
| regex_v8       | 25.1 ms                                                    | 25.3 ms: 1.01x slower                                                      |
| regex_compile  | 137 ms                                                     | 151 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                      | 1.01x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_process    | 61.2 ms                                                    | 53.9 ms: 1.13x faster                                                      |
| xml_etree_parse      | 162 ms                                                     | 145 ms: 1.12x faster                                                       |
| xml_etree_generate   | 87.4 ms                                                    | 78.8 ms: 1.11x faster                                                      |
| json_dumps           | 10.7 ms                                                    | 9.69 ms: 1.11x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                     | 97.8 ms: 1.10x faster                                                      |
| unpickle_pure_python | 218 us                                                     | 199 us: 1.10x faster                                                       |
| unpickle             | 15.1 us                                                    | 14.6 us: 1.03x faster                                                      |
| tomli_loads          | 2.12 sec                                                   | 2.07 sec: 1.02x faster                                                     |
| pickle_dict          | 34.8 us                                                    | 34.3 us: 1.02x faster                                                      |
| unpickle_list        | 5.34 us                                                    | 5.39 us: 1.01x slower                                                      |
| pickle_list          | 5.11 us                                                    | 5.21 us: 1.02x slower                                                      |
| json_loads           | 28.9 us                                                    | 29.5 us: 1.02x slower                                                      |
| pickle_pure_python   | 305 us                                                     | 313 us: 1.03x slower                                                       |
| pickle               | 11.5 us                                                    | 11.8 us: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                      | 1.04x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                      |
| python_startup_no_site | 7.11 ms                                                    | 7.17 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                      | 1.00x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|-----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.78 ms: 1.15x faster                                                      |
| genshi_text     | 23.7 ms                                                    | 22.6 ms: 1.05x faster                                                      |
| django_template | 34.8 ms                                                    | 40.4 ms: 1.16x slower                                                      |
| genshi_xml      | 51.6 ms                                                    | 60.0 ms: 1.16x slower                                                      |
| Geometric mean  | (ref)                                                      | 1.03x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.7 us: 1.49x faster                                                      |
| deepcopy                   | 367 us                                                     | 268 us: 1.37x faster                                                       |
| scimark_fft                | 392 ms                                                     | 307 ms: 1.28x faster                                                       |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.20 ms: 1.25x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                    | 2.69 us: 1.25x faster                                                      |
| richards                   | 50.9 ms                                                    | 40.9 ms: 1.24x faster                                                      |
| crypto_pyaes               | 77.5 ms                                                    | 65.4 ms: 1.18x faster                                                      |
| scimark_monte_carlo        | 69.2 ms                                                    | 58.4 ms: 1.18x faster                                                      |
| mako                       | 11.2 ms                                                    | 9.78 ms: 1.15x faster                                                      |
| spectral_norm              | 116 ms                                                     | 102 ms: 1.14x faster                                                       |
| xml_etree_process          | 61.2 ms                                                    | 53.9 ms: 1.13x faster                                                      |
| float                      | 78.9 ms                                                    | 69.8 ms: 1.13x faster                                                      |
| xml_etree_parse            | 162 ms                                                     | 145 ms: 1.12x faster                                                       |
| async_tree_none            | 378 ms                                                     | 338 ms: 1.12x faster                                                       |
| richards_super             | 57.4 ms                                                    | 51.4 ms: 1.12x faster                                                      |
| scimark_lu                 | 122 ms                                                     | 109 ms: 1.12x faster                                                       |
| xml_etree_generate         | 87.4 ms                                                    | 78.8 ms: 1.11x faster                                                      |
| json_dumps                 | 10.7 ms                                                    | 9.69 ms: 1.11x faster                                                      |
| bpe_tokeniser              | 5.02 sec                                                   | 4.54 sec: 1.11x faster                                                     |
| pathlib                    | 17.3 ms                                                    | 15.8 ms: 1.10x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                     | 97.8 ms: 1.10x faster                                                      |
| unpickle_pure_python       | 218 us                                                     | 199 us: 1.10x faster                                                       |
| pyflate                    | 484 ms                                                     | 441 ms: 1.10x faster                                                       |
| mdp                        | 2.79 sec                                                   | 2.54 sec: 1.10x faster                                                     |
| async_tree_memoization     | 463 ms                                                     | 426 ms: 1.09x faster                                                       |
| coverage                   | 93.1 ms                                                    | 85.9 ms: 1.08x faster                                                      |
| sqlite_synth               | 2.99 us                                                    | 2.76 us: 1.08x faster                                                      |
| fannkuch                   | 402 ms                                                     | 374 ms: 1.08x faster                                                       |
| regex_dna                  | 221 ms                                                     | 206 ms: 1.07x faster                                                       |
| async_tree_memoization_tg  | 444 ms                                                     | 415 ms: 1.07x faster                                                       |
| telco                      | 8.41 ms                                                    | 7.88 ms: 1.07x faster                                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 573 ms: 1.07x faster                                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 551 ms: 1.07x faster                                                       |
| regex_effbot               | 3.67 ms                                                    | 3.45 ms: 1.07x faster                                                      |
| nbody                      | 88.3 ms                                                    | 83.1 ms: 1.06x faster                                                      |
| gc_traversal               | 3.98 ms                                                    | 3.76 ms: 1.06x faster                                                      |
| async_tree_none_tg         | 336 ms                                                     | 321 ms: 1.05x faster                                                       |
| genshi_text                | 23.7 ms                                                    | 22.6 ms: 1.05x faster                                                      |
| chaos                      | 61.3 ms                                                    | 58.7 ms: 1.05x faster                                                      |
| thrift                     | 823 us                                                     | 795 us: 1.04x faster                                                       |
| unpickle                   | 15.1 us                                                    | 14.6 us: 1.03x faster                                                      |
| async_tree_io_tg           | 936 ms                                                     | 905 ms: 1.03x faster                                                       |
| typing_runtime_protocols   | 165 us                                                     | 159 us: 1.03x faster                                                       |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                       |
| scimark_sor                | 127 ms                                                     | 124 ms: 1.02x faster                                                       |
| tomli_loads                | 2.12 sec                                                   | 2.07 sec: 1.02x faster                                                     |
| meteor_contest             | 110 ms                                                     | 108 ms: 1.02x faster                                                       |
| asyncio_websockets         | 567 ms                                                     | 557 ms: 1.02x faster                                                       |
| pickle_dict                | 34.8 us                                                    | 34.3 us: 1.02x faster                                                      |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.82 sec: 1.01x faster                                                     |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                      |
| pprint_safe_repr           | 758 ms                                                     | 753 ms: 1.01x faster                                                       |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.00x faster                                                      |
| unpickle_list              | 5.34 us                                                    | 5.39 us: 1.01x slower                                                      |
| python_startup_no_site     | 7.11 ms                                                    | 7.17 ms: 1.01x slower                                                      |
| regex_v8                   | 25.1 ms                                                    | 25.3 ms: 1.01x slower                                                      |
| bench_mp_pool              | 23.9 ms                                                    | 24.2 ms: 1.01x slower                                                      |
| pickle_list                | 5.11 us                                                    | 5.21 us: 1.02x slower                                                      |
| json_loads                 | 28.9 us                                                    | 29.5 us: 1.02x slower                                                      |
| asyncio_tcp                | 508 ms                                                     | 520 ms: 1.02x slower                                                       |
| logging_simple             | 5.74 us                                                    | 5.88 us: 1.02x slower                                                      |
| pickle_pure_python         | 305 us                                                     | 313 us: 1.03x slower                                                       |
| async_generators           | 442 ms                                                     | 454 ms: 1.03x slower                                                       |
| pickle                     | 11.5 us                                                    | 11.8 us: 1.03x slower                                                      |
| nqueens                    | 81.4 ms                                                    | 84.1 ms: 1.03x slower                                                      |
| logging_format             | 6.47 us                                                    | 6.74 us: 1.04x slower                                                      |
| logging_silent             | 105 ns                                                     | 111 ns: 1.06x slower                                                       |
| coroutines                 | 23.2 ms                                                    | 24.7 ms: 1.06x slower                                                      |
| 2to3                       | 274 ms                                                     | 292 ms: 1.06x slower                                                       |
| bench_thread_pool          | 834 us                                                     | 895 us: 1.07x slower                                                       |
| raytrace                   | 267 ms                                                     | 289 ms: 1.08x slower                                                       |
| html5lib                   | 67.2 ms                                                    | 73.0 ms: 1.09x slower                                                      |
| deltablue                  | 3.25 ms                                                    | 3.57 ms: 1.10x slower                                                      |
| regex_compile              | 137 ms                                                     | 151 ms: 1.10x slower                                                       |
| sqlglot_normalize          | 110 ms                                                     | 126 ms: 1.14x slower                                                       |
| hexiom                     | 6.30 ms                                                    | 7.27 ms: 1.15x slower                                                      |
| generators                 | 29.6 ms                                                    | 34.3 ms: 1.16x slower                                                      |
| pycparser                  | 1.16 sec                                                   | 1.34 sec: 1.16x slower                                                     |
| django_template            | 34.8 ms                                                    | 40.4 ms: 1.16x slower                                                      |
| genshi_xml                 | 51.6 ms                                                    | 60.0 ms: 1.16x slower                                                      |
| sympy_expand               | 473 ms                                                     | 557 ms: 1.18x slower                                                       |
| sympy_str                  | 282 ms                                                     | 341 ms: 1.21x slower                                                       |
| sqlglot_optimize           | 55.5 ms                                                    | 67.8 ms: 1.22x slower                                                      |
| docutils                   | 2.83 sec                                                   | 3.46 sec: 1.22x slower                                                     |
| go                         | 145 ms                                                     | 178 ms: 1.23x slower                                                       |
| tornado_http               | 94.6 ms                                                    | 119 ms: 1.25x slower                                                       |
| sqlglot_parse              | 1.32 ms                                                    | 1.69 ms: 1.28x slower                                                      |
| sqlglot_transpile          | 1.63 ms                                                    | 2.15 ms: 1.31x slower                                                      |
| sympy_integrate            | 20.5 ms                                                    | 27.6 ms: 1.35x slower                                                      |
| sympy_sum                  | 156 ms                                                     | 215 ms: 1.38x slower                                                       |
| pylint                     | 317 ms                                                     | 482 ms: 1.52x slower                                                       |
| Geometric mean             | (ref)                                                      | 1.00x faster                                                               |

Benchmark hidden because not significant (4): json, create_gc_cycles, pprint_pformat, async_tree_io
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240909-3.14.0a0-c66bd3e-JIT/bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e.json: unpack_sequence

# HPT report

- Reliability score: 87.96% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.18x