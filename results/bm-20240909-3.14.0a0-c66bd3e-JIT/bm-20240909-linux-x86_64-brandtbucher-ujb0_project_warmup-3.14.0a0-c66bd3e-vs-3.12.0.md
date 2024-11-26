# Results vs. 3.12.0

- fork: brandtbucher
- ref: ujb0_project_warmup
- machine: linux-x86_64
- commit hash: c66bd3e
- commit date: 2024-09-09
- overall geometric mean: 1.045x faster
- HPT reliability: 99.19%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 292 ms: 1.06x slower                                                       |
| docutils       | 2.77 sec                                               | 3.46 sec: 1.25x slower                                                     |
| tornado_http   | 103 ms                                                 | 119 ms: 1.16x slower                                                       |
| Geometric mean | (ref)                                                  | 1.15x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 321 ms: 1.40x faster                                                       |
| async_tree_none            | 472 ms                                                 | 338 ms: 1.39x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 415 ms: 1.39x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 426 ms: 1.36x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 551 ms: 1.32x faster                                                       |
| async_tree_io_tg           | 1.18 sec                                               | 905 ms: 1.31x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 573 ms: 1.27x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 951 ms: 1.22x faster                                                       |
| Geometric mean             | (ref)                                                  | 1.33x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.8 ms: 1.21x faster                                                      |
| nbody          | 97.0 ms                                                | 83.1 ms: 1.17x faster                                                      |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.13x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.45 ms: 1.05x faster                                                      |
| regex_dna      | 212 ms                                                 | 206 ms: 1.03x faster                                                       |
| regex_compile  | 148 ms                                                 | 151 ms: 1.02x slower                                                       |
| regex_v8       | 23.1 ms                                                | 25.3 ms: 1.10x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 230 us                                                 | 199 us: 1.16x faster                                                       |
| xml_etree_process    | 61.7 ms                                                | 53.9 ms: 1.14x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 78.8 ms: 1.13x faster                                                      |
| tomli_loads          | 2.33 sec                                               | 2.07 sec: 1.13x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 145 ms: 1.10x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                 | 97.8 ms: 1.09x faster                                                      |
| unpickle             | 15.9 us                                                | 14.6 us: 1.08x faster                                                      |
| json_dumps           | 10.4 ms                                                | 9.69 ms: 1.07x faster                                                      |
| pickle_dict          | 35.5 us                                                | 34.3 us: 1.04x faster                                                      |
| pickle_pure_python   | 324 us                                                 | 313 us: 1.03x faster                                                       |
| pickle               | 11.6 us                                                | 11.8 us: 1.02x slower                                                      |
| unpickle_list        | 5.29 us                                                | 5.39 us: 1.02x slower                                                      |
| pickle_list          | 5.08 us                                                | 5.21 us: 1.02x slower                                                      |
| json_loads           | 28.5 us                                                | 29.5 us: 1.04x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.17 ms: 1.03x slower                                                      |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.78 ms: 1.22x faster                                                      |
| django_template | 34.6 ms                                                | 40.4 ms: 1.17x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.7 us: 1.52x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 321 ms: 1.40x faster                                                       |
| async_tree_none            | 472 ms                                                 | 338 ms: 1.39x faster                                                       |
| deepcopy                   | 371 us                                                 | 268 us: 1.39x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 415 ms: 1.39x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 426 ms: 1.36x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 551 ms: 1.32x faster                                                       |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 905 ms: 1.31x faster                                                       |
| scimark_monte_carlo        | 75.1 ms                                                | 58.4 ms: 1.29x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 573 ms: 1.27x faster                                                       |
| crypto_pyaes               | 81.9 ms                                                | 65.4 ms: 1.25x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                                      |
| scimark_fft                | 382 ms                                                 | 307 ms: 1.24x faster                                                       |
| pathlib                    | 19.3 ms                                                | 15.8 ms: 1.23x faster                                                      |
| mako                       | 11.9 ms                                                | 9.78 ms: 1.22x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 951 ms: 1.22x faster                                                       |
| float                      | 84.7 ms                                                | 69.8 ms: 1.21x faster                                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.20 ms: 1.20x faster                                                      |
| nbody                      | 97.0 ms                                                | 83.1 ms: 1.17x faster                                                      |
| unpickle_pure_python       | 230 us                                                 | 199 us: 1.16x faster                                                       |
| xml_etree_process          | 61.7 ms                                                | 53.9 ms: 1.14x faster                                                      |
| chaos                      | 67.0 ms                                                | 58.7 ms: 1.14x faster                                                      |
| xml_etree_generate         | 89.2 ms                                                | 78.8 ms: 1.13x faster                                                      |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.13x faster                                                       |
| tomli_loads                | 2.33 sec                                               | 2.07 sec: 1.13x faster                                                     |
| richards                   | 45.8 ms                                                | 40.9 ms: 1.12x faster                                                      |
| fannkuch                   | 417 ms                                                 | 374 ms: 1.12x faster                                                       |
| xml_etree_parse            | 159 ms                                                 | 145 ms: 1.10x faster                                                       |
| logging_simple             | 6.46 us                                                | 5.88 us: 1.10x faster                                                      |
| pyflate                    | 482 ms                                                 | 441 ms: 1.09x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                 | 97.8 ms: 1.09x faster                                                      |
| unpickle                   | 15.9 us                                                | 14.6 us: 1.08x faster                                                      |
| scimark_lu                 | 118 ms                                                 | 109 ms: 1.08x faster                                                       |
| raytrace                   | 312 ms                                                 | 289 ms: 1.08x faster                                                       |
| logging_format             | 7.23 us                                                | 6.74 us: 1.07x faster                                                      |
| json_dumps                 | 10.4 ms                                                | 9.69 ms: 1.07x faster                                                      |
| regex_effbot               | 3.61 ms                                                | 3.45 ms: 1.05x faster                                                      |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                       |
| deltablue                  | 3.72 ms                                                | 3.57 ms: 1.04x faster                                                      |
| scimark_sor                | 129 ms                                                 | 124 ms: 1.04x faster                                                       |
| pickle_dict                | 35.5 us                                                | 34.3 us: 1.04x faster                                                      |
| mdp                        | 2.63 sec                                               | 2.54 sec: 1.03x faster                                                     |
| pickle_pure_python         | 324 us                                                 | 313 us: 1.03x faster                                                       |
| pprint_safe_repr           | 776 ms                                                 | 753 ms: 1.03x faster                                                       |
| regex_dna                  | 212 ms                                                 | 206 ms: 1.03x faster                                                       |
| sqlite_synth               | 2.83 us                                                | 2.76 us: 1.02x faster                                                      |
| async_generators           | 463 ms                                                 | 454 ms: 1.02x faster                                                       |
| gc_traversal               | 3.79 ms                                                | 3.76 ms: 1.01x faster                                                      |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                       |
| bench_mp_pool              | 24.0 ms                                                | 24.2 ms: 1.01x slower                                                      |
| typing_runtime_protocols   | 158 us                                                 | 159 us: 1.01x slower                                                       |
| nqueens                    | 83.3 ms                                                | 84.1 ms: 1.01x slower                                                      |
| asyncio_websockets         | 551 ms                                                 | 557 ms: 1.01x slower                                                       |
| regex_compile              | 148 ms                                                 | 151 ms: 1.02x slower                                                       |
| pickle                     | 11.6 us                                                | 11.8 us: 1.02x slower                                                      |
| unpickle_list              | 5.29 us                                                | 5.39 us: 1.02x slower                                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.82 sec: 1.02x slower                                                     |
| pickle_list                | 5.08 us                                                | 5.21 us: 1.02x slower                                                      |
| python_startup_no_site     | 6.94 ms                                                | 7.17 ms: 1.03x slower                                                      |
| json_loads                 | 28.5 us                                                | 29.5 us: 1.04x slower                                                      |
| asyncio_tcp                | 491 ms                                                 | 520 ms: 1.06x slower                                                       |
| logging_silent             | 104 ns                                                 | 111 ns: 1.06x slower                                                       |
| 2to3                       | 274 ms                                                 | 292 ms: 1.06x slower                                                       |
| bench_thread_pool          | 842 us                                                 | 895 us: 1.06x slower                                                       |
| coroutines                 | 23.2 ms                                                | 24.7 ms: 1.06x slower                                                      |
| regex_v8                   | 23.1 ms                                                | 25.3 ms: 1.10x slower                                                      |
| generators                 | 31.2 ms                                                | 34.3 ms: 1.10x slower                                                      |
| telco                      | 7.10 ms                                                | 7.88 ms: 1.11x slower                                                      |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                      |
| hexiom                     | 6.41 ms                                                | 7.27 ms: 1.13x slower                                                      |
| pycparser                  | 1.18 sec                                               | 1.34 sec: 1.14x slower                                                     |
| sqlglot_normalize          | 110 ms                                                 | 126 ms: 1.14x slower                                                       |
| sympy_str                  | 300 ms                                                 | 341 ms: 1.14x slower                                                       |
| tornado_http               | 103 ms                                                 | 119 ms: 1.16x slower                                                       |
| sympy_expand               | 478 ms                                                 | 557 ms: 1.16x slower                                                       |
| django_template            | 34.6 ms                                                | 40.4 ms: 1.17x slower                                                      |
| coverage                   | 72.7 ms                                                | 85.9 ms: 1.18x slower                                                      |
| create_gc_cycles           | 1.48 ms                                                | 1.81 ms: 1.23x slower                                                      |
| sqlglot_optimize           | 54.8 ms                                                | 67.8 ms: 1.24x slower                                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.69 ms: 1.24x slower                                                      |
| docutils                   | 2.77 sec                                               | 3.46 sec: 1.25x slower                                                     |
| sympy_sum                  | 169 ms                                                 | 215 ms: 1.27x slower                                                       |
| sqlglot_transpile          | 1.68 ms                                                | 2.15 ms: 1.28x slower                                                      |
| go                         | 139 ms                                                 | 178 ms: 1.28x slower                                                       |
| sympy_integrate            | 21.4 ms                                                | 27.6 ms: 1.29x slower                                                      |
| unpack_sequence            | 54.0 ns                                                | 138 ns: 2.56x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (3): pprint_pformat, richards_super, json
Ignored benchmarks (8) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240909-3.14.0a0-c66bd3e-JIT/bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.045x faster
# HPT report

- Reliability score: 99.19% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.15x