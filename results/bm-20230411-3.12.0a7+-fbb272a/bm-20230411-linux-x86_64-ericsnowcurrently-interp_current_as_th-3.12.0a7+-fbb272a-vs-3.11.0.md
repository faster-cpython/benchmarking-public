
# Results vs. 3.11.0

- fork: ericsnowcurrently
- ref: interp_current_as_th
- machine: linux-x86_64
- commit hash: fbb272a
- commit date: 2023-04-11
- overall geometric mean: 1.05x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230411-linux-x86_64-ericsnowcurrently-interp_current_as_th-3.12.0a7+-fbb272a |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 250 ms: 1.03x faster                                                              |
| docutils       | 2.59 sec                                                            | 2.52 sec: 1.03x faster                                                            |
| html5lib       | 64.0 ms                                                             | 61.3 ms: 1.04x faster                                                             |
| tornado_http   | 96.7 ms                                                             | 90.5 ms: 1.07x faster                                                             |
| Geometric mean | (ref)                                                               | 1.03x faster                                                                      |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230411-linux-x86_64-ericsnowcurrently-interp_current_as_th-3.12.0a7+-fbb272a |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 82.7 ms: 1.17x faster                                                             |
| pidigits       | 197 ms                                                              | 188 ms: 1.05x faster                                                              |
| float          | 76.0 ms                                                             | 73.0 ms: 1.04x faster                                                             |
| Geometric mean | (ref)                                                               | 1.08x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230411-linux-x86_64-ericsnowcurrently-interp_current_as_th-3.12.0a7+-fbb272a |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                              | 131 ms: 1.04x faster                                                              |
| regex_v8       | 22.0 ms                                                             | 22.5 ms: 1.02x slower                                                             |
| regex_effbot   | 3.32 ms                                                             | 3.57 ms: 1.08x slower                                                             |
| regex_dna      | 196 ms                                                              | 214 ms: 1.09x slower                                                              |
| Geometric mean | (ref)                                                               | 1.04x slower                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230411-linux-x86_64-ericsnowcurrently-interp_current_as_th-3.12.0a7+-fbb272a |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 12.5 ms                                                             | 9.40 ms: 1.33x faster                                                             |
| unpickle_pure_python | 228 us                                                              | 202 us: 1.13x faster                                                              |
| xml_etree_iterparse  | 108 ms                                                              | 98.7 ms: 1.09x faster                                                             |
| xml_etree_parse      | 162 ms                                                              | 150 ms: 1.08x faster                                                              |
| pickle_pure_python   | 307 us                                                              | 284 us: 1.08x faster                                                              |
| json_loads           | 26.2 us                                                             | 24.4 us: 1.07x faster                                                             |
| unpickle_list        | 4.96 us                                                             | 4.67 us: 1.06x faster                                                             |
| unpickle             | 13.2 us                                                             | 13.1 us: 1.01x faster                                                             |
| xml_etree_process    | 54.1 ms                                                             | 55.3 ms: 1.02x slower                                                             |
| pickle_dict          | 30.9 us                                                             | 32.1 us: 1.04x slower                                                             |
| xml_etree_generate   | 76.5 ms                                                             | 80.2 ms: 1.05x slower                                                             |
| pickle_list          | 4.03 us                                                             | 4.34 us: 1.08x slower                                                             |
| pickle               | 9.79 us                                                             | 10.6 us: 1.08x slower                                                             |
| Geometric mean       | (ref)                                                               | 1.04x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230411-linux-x86_64-ericsnowcurrently-interp_current_as_th-3.12.0a7+-fbb272a |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 8.80 ms: 1.04x slower                                                             |
| python_startup_no_site | 5.98 ms                                                             | 6.50 ms: 1.09x slower                                                             |
| Geometric mean         | (ref)                                                               | 1.06x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230411-linux-x86_64-ericsnowcurrently-interp_current_as_th-3.12.0a7+-fbb272a |
|-----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                             | 47.1 ms: 1.10x faster                                                             |
| genshi_text     | 21.8 ms                                                             | 21.2 ms: 1.03x faster                                                             |
| django_template | 32.9 ms                                                             | 32.0 ms: 1.03x faster                                                             |
| mako            | 9.82 ms                                                             | 9.95 ms: 1.01x slower                                                             |
| Geometric mean  | (ref)                                                               | 1.04x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230411-linux-x86_64-ericsnowcurrently-interp_current_as_th-3.12.0a7+-fbb272a |
|-------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 73.4 ms                                                             | 29.2 ms: 2.51x faster                                                             |
| asyncio_tcp             | 888 ms                                                              | 507 ms: 1.75x faster                                                              |
| json_dumps              | 12.5 ms                                                             | 9.40 ms: 1.33x faster                                                             |
| mypy2                   | 422 ms                                                              | 333 ms: 1.27x faster                                                              |
| nbody                   | 96.7 ms                                                             | 82.7 ms: 1.17x faster                                                             |
| unpack_sequence         | 49.5 ns                                                             | 42.3 ns: 1.17x faster                                                             |
| deltablue               | 3.66 ms                                                             | 3.19 ms: 1.15x faster                                                             |
| coroutines              | 26.3 ms                                                             | 23.0 ms: 1.14x faster                                                             |
| sqlglot_parse           | 1.36 ms                                                             | 1.20 ms: 1.13x faster                                                             |
| unpickle_pure_python    | 228 us                                                              | 202 us: 1.13x faster                                                              |
| sqlglot_transpile       | 1.65 ms                                                             | 1.49 ms: 1.11x faster                                                             |
| genshi_xml              | 51.8 ms                                                             | 47.1 ms: 1.10x faster                                                             |
| xml_etree_iterparse     | 108 ms                                                              | 98.7 ms: 1.09x faster                                                             |
| scimark_fft             | 328 ms                                                              | 300 ms: 1.09x faster                                                              |
| xml_etree_parse         | 162 ms                                                              | 150 ms: 1.08x faster                                                              |
| logging_simple          | 6.09 us                                                             | 5.62 us: 1.08x faster                                                             |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.12 ms: 1.08x faster                                                             |
| deepcopy_memo           | 36.4 us                                                             | 33.6 us: 1.08x faster                                                             |
| hexiom                  | 6.48 ms                                                             | 5.99 ms: 1.08x faster                                                             |
| pickle_pure_python      | 307 us                                                              | 284 us: 1.08x faster                                                              |
| logging_format          | 6.64 us                                                             | 6.18 us: 1.07x faster                                                             |
| json_loads              | 26.2 us                                                             | 24.4 us: 1.07x faster                                                             |
| sqlglot_optimize        | 53.4 ms                                                             | 49.9 ms: 1.07x faster                                                             |
| tornado_http            | 96.7 ms                                                             | 90.5 ms: 1.07x faster                                                             |
| sqlglot_normalize       | 108 ms                                                              | 101 ms: 1.07x faster                                                              |
| nqueens                 | 84.0 ms                                                             | 78.8 ms: 1.07x faster                                                             |
| raytrace                | 292 ms                                                              | 275 ms: 1.06x faster                                                              |
| unpickle_list           | 4.96 us                                                             | 4.67 us: 1.06x faster                                                             |
| chaos                   | 68.0 ms                                                             | 64.1 ms: 1.06x faster                                                             |
| spectral_norm           | 99.5 ms                                                             | 94.1 ms: 1.06x faster                                                             |
| deepcopy                | 339 us                                                              | 321 us: 1.06x faster                                                              |
| mdp                     | 2.64 sec                                                            | 2.50 sec: 1.06x faster                                                            |
| richards                | 45.7 ms                                                             | 43.2 ms: 1.06x faster                                                             |
| scimark_sor             | 115 ms                                                              | 109 ms: 1.05x faster                                                              |
| aiohttp                 | 1.05 ms                                                             | 1.00 ms: 1.05x faster                                                             |
| pprint_pformat          | 1.45 sec                                                            | 1.38 sec: 1.05x faster                                                            |
| comprehensions          | 22.2 us                                                             | 21.2 us: 1.05x faster                                                             |
| logging_silent          | 98.7 ns                                                             | 94.3 ns: 1.05x faster                                                             |
| meteor_contest          | 106 ms                                                              | 101 ms: 1.05x faster                                                              |
| pidigits                | 197 ms                                                              | 188 ms: 1.05x faster                                                              |
| bench_thread_pool       | 820 us                                                              | 785 us: 1.04x faster                                                              |
| sympy_expand            | 477 ms                                                              | 457 ms: 1.04x faster                                                              |
| html5lib                | 64.0 ms                                                             | 61.3 ms: 1.04x faster                                                             |
| gunicorn                | 1.13 ms                                                             | 1.08 ms: 1.04x faster                                                             |
| float                   | 76.0 ms                                                             | 73.0 ms: 1.04x faster                                                             |
| regex_compile           | 137 ms                                                              | 131 ms: 1.04x faster                                                              |
| sympy_integrate         | 21.0 ms                                                             | 20.3 ms: 1.04x faster                                                             |
| sympy_str               | 291 ms                                                              | 282 ms: 1.03x faster                                                              |
| coverage                | 101 ms                                                              | 97.8 ms: 1.03x faster                                                             |
| genshi_text             | 21.8 ms                                                             | 21.2 ms: 1.03x faster                                                             |
| deepcopy_reduce         | 2.96 us                                                             | 2.87 us: 1.03x faster                                                             |
| json                    | 4.86 ms                                                             | 4.72 ms: 1.03x faster                                                             |
| pprint_safe_repr        | 701 ms                                                              | 682 ms: 1.03x faster                                                              |
| 2to3                    | 257 ms                                                              | 250 ms: 1.03x faster                                                              |
| django_template         | 32.9 ms                                                             | 32.0 ms: 1.03x faster                                                             |
| telco                   | 6.59 ms                                                             | 6.41 ms: 1.03x faster                                                             |
| docutils                | 2.59 sec                                                            | 2.52 sec: 1.03x faster                                                            |
| async_tree_memoization  | 621 ms                                                              | 605 ms: 1.03x faster                                                              |
| scimark_lu              | 108 ms                                                              | 106 ms: 1.02x faster                                                              |
| dulwich_log             | 63.6 ms                                                             | 62.3 ms: 1.02x faster                                                             |
| sympy_sum               | 167 ms                                                              | 164 ms: 1.02x faster                                                              |
| sqlalchemy_imperative   | 18.0 ms                                                             | 17.7 ms: 1.02x faster                                                             |
| async_tree_cpu_io_mixed | 736 ms                                                              | 721 ms: 1.02x faster                                                              |
| sqlalchemy_declarative  | 138 ms                                                              | 136 ms: 1.02x faster                                                              |
| async_tree_none         | 525 ms                                                              | 516 ms: 1.02x faster                                                              |
| scimark_monte_carlo     | 67.8 ms                                                             | 66.6 ms: 1.02x faster                                                             |
| pathlib                 | 18.2 ms                                                             | 18.0 ms: 1.01x faster                                                             |
| unpickle                | 13.2 us                                                             | 13.1 us: 1.01x faster                                                             |
| create_gc_cycles        | 1.48 ms                                                             | 1.49 ms: 1.01x slower                                                             |
| go                      | 138 ms                                                              | 139 ms: 1.01x slower                                                              |
| pyflate                 | 414 ms                                                              | 419 ms: 1.01x slower                                                              |
| mako                    | 9.82 ms                                                             | 9.95 ms: 1.01x slower                                                             |
| xml_etree_process       | 54.1 ms                                                             | 55.3 ms: 1.02x slower                                                             |
| fannkuch                | 384 ms                                                              | 392 ms: 1.02x slower                                                              |
| regex_v8                | 22.0 ms                                                             | 22.5 ms: 1.02x slower                                                             |
| sqlite_synth            | 2.51 us                                                             | 2.60 us: 1.03x slower                                                             |
| python_startup          | 8.49 ms                                                             | 8.80 ms: 1.04x slower                                                             |
| pickle_dict             | 30.9 us                                                             | 32.1 us: 1.04x slower                                                             |
| xml_etree_generate      | 76.5 ms                                                             | 80.2 ms: 1.05x slower                                                             |
| regex_effbot            | 3.32 ms                                                             | 3.57 ms: 1.08x slower                                                             |
| pickle_list             | 4.03 us                                                             | 4.34 us: 1.08x slower                                                             |
| pickle                  | 9.79 us                                                             | 10.6 us: 1.08x slower                                                             |
| regex_dna               | 196 ms                                                              | 214 ms: 1.09x slower                                                              |
| python_startup_no_site  | 5.98 ms                                                             | 6.50 ms: 1.09x slower                                                             |
| async_generators        | 361 ms                                                              | 405 ms: 1.12x slower                                                              |
| gc_traversal            | 3.63 ms                                                             | 4.30 ms: 1.19x slower                                                             |
| dask                    | 368 ms                                                              | 493 ms: 1.34x slower                                                              |
| Geometric mean          | (ref)                                                               | 1.05x faster                                                                      |

Benchmark hidden because not significant (7): pycparser, djangocms, chameleon, bench_mp_pool, crypto_pyaes, thrift, async_tree_io
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: flaskblogging, pylint
