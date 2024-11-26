# Results vs. 3.12.0

- fork: brandtbucher
- ref: ujb0_project_warmup
- machine: linux-x86_64
- commit hash: f67fedc
- commit date: 2024-09-09
- overall geometric mean: 1.035x faster
- HPT reliability: 88.26%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 292 ms: 1.06x slower                                                       |
| docutils       | 2.77 sec                                               | 3.47 sec: 1.25x slower                                                     |
| tornado_http   | 103 ms                                                 | 119 ms: 1.16x slower                                                       |
| Geometric mean | (ref)                                                  | 1.16x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 318 ms: 1.41x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 409 ms: 1.40x faster                                                       |
| async_tree_none            | 472 ms                                                 | 339 ms: 1.39x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 422 ms: 1.37x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 550 ms: 1.32x faster                                                       |
| async_tree_io_tg           | 1.18 sec                                               | 919 ms: 1.29x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 571 ms: 1.27x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 947 ms: 1.22x faster                                                       |
| Geometric mean             | (ref)                                                  | 1.33x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.9 ms: 1.21x faster                                                      |
| nbody          | 97.0 ms                                                | 82.2 ms: 1.18x faster                                                      |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.13x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 212 ms                                                 | 215 ms: 1.01x slower                                                       |
| regex_compile  | 148 ms                                                 | 155 ms: 1.04x slower                                                       |
| regex_effbot   | 3.61 ms                                                | 3.77 ms: 1.04x slower                                                      |
| regex_v8       | 23.1 ms                                                | 25.9 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                  | 1.05x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 230 us                                                 | 191 us: 1.20x faster                                                       |
| xml_etree_process    | 61.7 ms                                                | 54.0 ms: 1.14x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 78.1 ms: 1.14x faster                                                      |
| tomli_loads          | 2.33 sec                                               | 2.06 sec: 1.13x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 144 ms: 1.11x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                 | 98.2 ms: 1.09x faster                                                      |
| unpickle             | 15.9 us                                                | 14.7 us: 1.08x faster                                                      |
| json_dumps           | 10.4 ms                                                | 9.90 ms: 1.05x faster                                                      |
| pickle_pure_python   | 324 us                                                 | 314 us: 1.03x faster                                                       |
| pickle               | 11.6 us                                                | 11.4 us: 1.02x faster                                                      |
| pickle_dict          | 35.5 us                                                | 35.2 us: 1.01x faster                                                      |
| pickle_list          | 5.08 us                                                | 5.19 us: 1.02x slower                                                      |
| json_loads           | 28.5 us                                                | 29.5 us: 1.04x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                               |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.19 ms: 1.04x slower                                                      |
| python_startup         | 9.55 ms                                                | 10.8 ms: 1.13x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.65 ms: 1.23x faster                                                      |
| django_template | 34.6 ms                                                | 38.8 ms: 1.12x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 27.1 us: 1.50x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 318 ms: 1.41x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 409 ms: 1.40x faster                                                       |
| deepcopy                   | 371 us                                                 | 267 us: 1.39x faster                                                       |
| async_tree_none            | 472 ms                                                 | 339 ms: 1.39x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 422 ms: 1.37x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 550 ms: 1.32x faster                                                       |
| scimark_monte_carlo        | 75.1 ms                                                | 58.1 ms: 1.29x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 919 ms: 1.29x faster                                                       |
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 571 ms: 1.27x faster                                                       |
| mako                       | 11.9 ms                                                | 9.65 ms: 1.23x faster                                                      |
| scimark_fft                | 382 ms                                                 | 312 ms: 1.22x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 947 ms: 1.22x faster                                                       |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                                      |
| float                      | 84.7 ms                                                | 69.9 ms: 1.21x faster                                                      |
| unpickle_pure_python       | 230 us                                                 | 191 us: 1.20x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                | 2.79 us: 1.20x faster                                                      |
| crypto_pyaes               | 81.9 ms                                                | 68.2 ms: 1.20x faster                                                      |
| nbody                      | 97.0 ms                                                | 82.2 ms: 1.18x faster                                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.38 ms: 1.15x faster                                                      |
| xml_etree_process          | 61.7 ms                                                | 54.0 ms: 1.14x faster                                                      |
| xml_etree_generate         | 89.2 ms                                                | 78.1 ms: 1.14x faster                                                      |
| raytrace                   | 312 ms                                                 | 275 ms: 1.13x faster                                                       |
| tomli_loads                | 2.33 sec                                               | 2.06 sec: 1.13x faster                                                     |
| deltablue                  | 3.72 ms                                                | 3.29 ms: 1.13x faster                                                      |
| logging_format             | 7.23 us                                                | 6.43 us: 1.12x faster                                                      |
| fannkuch                   | 417 ms                                                 | 372 ms: 1.12x faster                                                       |
| xml_etree_parse            | 159 ms                                                 | 144 ms: 1.11x faster                                                       |
| logging_simple             | 6.46 us                                                | 5.88 us: 1.10x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                 | 98.2 ms: 1.09x faster                                                      |
| unpickle                   | 15.9 us                                                | 14.7 us: 1.08x faster                                                      |
| scimark_lu                 | 118 ms                                                 | 109 ms: 1.08x faster                                                       |
| chaos                      | 67.0 ms                                                | 62.3 ms: 1.07x faster                                                      |
| spectral_norm              | 115 ms                                                 | 107 ms: 1.07x faster                                                       |
| scimark_sor                | 129 ms                                                 | 122 ms: 1.06x faster                                                       |
| json_dumps                 | 10.4 ms                                                | 9.90 ms: 1.05x faster                                                      |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                       |
| pickle_pure_python         | 324 us                                                 | 314 us: 1.03x faster                                                       |
| pyflate                    | 482 ms                                                 | 471 ms: 1.02x faster                                                       |
| sqlite_synth               | 2.83 us                                                | 2.77 us: 1.02x faster                                                      |
| pickle                     | 11.6 us                                                | 11.4 us: 1.02x faster                                                      |
| pprint_safe_repr           | 776 ms                                                 | 761 ms: 1.02x faster                                                       |
| async_generators           | 463 ms                                                 | 455 ms: 1.02x faster                                                       |
| logging_silent             | 104 ns                                                 | 103 ns: 1.01x faster                                                       |
| pickle_dict                | 35.5 us                                                | 35.2 us: 1.01x faster                                                      |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                       |
| gc_traversal               | 3.79 ms                                                | 3.78 ms: 1.00x faster                                                      |
| nqueens                    | 83.3 ms                                                | 84.0 ms: 1.01x slower                                                      |
| asyncio_websockets         | 551 ms                                                 | 557 ms: 1.01x slower                                                       |
| regex_dna                  | 212 ms                                                 | 215 ms: 1.01x slower                                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.82 sec: 1.02x slower                                                     |
| pickle_list                | 5.08 us                                                | 5.19 us: 1.02x slower                                                      |
| mdp                        | 2.63 sec                                               | 2.72 sec: 1.03x slower                                                     |
| coroutines                 | 23.2 ms                                                | 23.9 ms: 1.03x slower                                                      |
| python_startup_no_site     | 6.94 ms                                                | 7.19 ms: 1.04x slower                                                      |
| json_loads                 | 28.5 us                                                | 29.5 us: 1.04x slower                                                      |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                       |
| regex_compile              | 148 ms                                                 | 155 ms: 1.04x slower                                                       |
| regex_effbot               | 3.61 ms                                                | 3.77 ms: 1.04x slower                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.66 sec: 1.06x slower                                                     |
| 2to3                       | 274 ms                                                 | 292 ms: 1.06x slower                                                       |
| asyncio_tcp                | 491 ms                                                 | 522 ms: 1.06x slower                                                       |
| bench_thread_pool          | 842 us                                                 | 898 us: 1.07x slower                                                       |
| telco                      | 7.10 ms                                                | 7.75 ms: 1.09x slower                                                      |
| pycparser                  | 1.18 sec                                               | 1.30 sec: 1.11x slower                                                     |
| hexiom                     | 6.41 ms                                                | 7.14 ms: 1.11x slower                                                      |
| generators                 | 31.2 ms                                                | 34.8 ms: 1.11x slower                                                      |
| regex_v8                   | 23.1 ms                                                | 25.9 ms: 1.12x slower                                                      |
| django_template            | 34.6 ms                                                | 38.8 ms: 1.12x slower                                                      |
| python_startup             | 9.55 ms                                                | 10.8 ms: 1.13x slower                                                      |
| sqlglot_normalize          | 110 ms                                                 | 125 ms: 1.13x slower                                                       |
| sympy_str                  | 300 ms                                                 | 341 ms: 1.14x slower                                                       |
| tornado_http               | 103 ms                                                 | 119 ms: 1.16x slower                                                       |
| sympy_expand               | 478 ms                                                 | 556 ms: 1.16x slower                                                       |
| richards                   | 45.8 ms                                                | 53.8 ms: 1.17x slower                                                      |
| coverage                   | 72.7 ms                                                | 85.4 ms: 1.18x slower                                                      |
| richards_super             | 51.5 ms                                                | 60.8 ms: 1.18x slower                                                      |
| create_gc_cycles           | 1.48 ms                                                | 1.79 ms: 1.21x slower                                                      |
| sqlglot_optimize           | 54.8 ms                                                | 67.1 ms: 1.22x slower                                                      |
| docutils                   | 2.77 sec                                               | 3.47 sec: 1.25x slower                                                     |
| sympy_sum                  | 169 ms                                                 | 214 ms: 1.27x slower                                                       |
| sqlglot_parse              | 1.36 ms                                                | 1.73 ms: 1.27x slower                                                      |
| sympy_integrate            | 21.4 ms                                                | 27.3 ms: 1.27x slower                                                      |
| go                         | 139 ms                                                 | 178 ms: 1.27x slower                                                       |
| sqlglot_transpile          | 1.68 ms                                                | 2.17 ms: 1.29x slower                                                      |
| unpack_sequence            | 54.0 ns                                                | 148 ns: 2.75x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                               |

Benchmark hidden because not significant (3): bench_mp_pool, unpickle_list, json
Ignored benchmarks (8) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240909-3.14.0a0-f67fedc-JIT/bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.035x faster
# HPT report

- Reliability score: 88.26% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.13x