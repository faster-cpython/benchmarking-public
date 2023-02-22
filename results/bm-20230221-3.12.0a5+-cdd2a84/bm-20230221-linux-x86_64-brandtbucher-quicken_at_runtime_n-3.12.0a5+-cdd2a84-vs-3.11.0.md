
# Results vs. 3.11.0

- fork: brandtbucher
- ref: quicken_at_runtime_n
- machine: linux-x86_64
- commit hash: cdd2a84
- commit date: 2023-02-21
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230221-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a5+-cdd2a84 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 247 ms: 1.05x faster                                                         |
| chameleon      | 6.38 ms                                                | 6.42 ms: 1.01x slower                                                        |
| docutils       | 2.60 sec                                               | 2.53 sec: 1.03x faster                                                       |
| html5lib       | 64.8 ms                                                | 61.3 ms: 1.06x faster                                                        |
| tornado_http   | 96.5 ms                                                | 94.7 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230221-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a5+-cdd2a84 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.6 ms: 1.06x faster                                                        |
| pidigits       | 197 ms                                                 | 192 ms: 1.02x faster                                                         |
| nbody          | 90.0 ms                                                | 96.0 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230221-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a5+-cdd2a84 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 129 ms: 1.06x faster                                                         |
| regex_effbot   | 3.46 ms                                                | 3.36 ms: 1.03x faster                                                        |
| regex_v8       | 22.2 ms                                                | 22.1 ms: 1.01x faster                                                        |
| regex_dna      | 203 ms                                                 | 210 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230221-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a5+-cdd2a84 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.45 ms: 1.31x faster                                                        |
| unpickle_pure_python | 227 us                                                 | 195 us: 1.17x faster                                                         |
| json_loads           | 26.1 us                                                | 23.6 us: 1.10x faster                                                        |
| pickle_pure_python   | 308 us                                                 | 283 us: 1.09x faster                                                         |
| xml_etree_parse      | 160 ms                                                 | 149 ms: 1.08x faster                                                         |
| xml_etree_iterparse  | 104 ms                                                 | 99.3 ms: 1.05x faster                                                        |
| xml_etree_process    | 53.7 ms                                                | 54.6 ms: 1.02x slower                                                        |
| pickle_list          | 4.14 us                                                | 4.30 us: 1.04x slower                                                        |
| pickle               | 9.90 us                                                | 10.3 us: 1.04x slower                                                        |
| pickle_dict          | 31.2 us                                                | 32.4 us: 1.04x slower                                                        |
| xml_etree_generate   | 75.9 ms                                                | 80.0 ms: 1.05x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (2): unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230221-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a5+-cdd2a84 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.81 ms: 1.03x slower                                                        |
| python_startup_no_site | 6.04 ms                                                | 6.34 ms: 1.05x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230221-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a5+-cdd2a84 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 46.5 ms: 1.11x faster                                                        |
| genshi_text     | 21.5 ms                                                | 20.8 ms: 1.03x faster                                                        |
| django_template | 32.3 ms                                                | 32.9 ms: 1.02x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230221-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a5+-cdd2a84 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.5 ms: 2.49x faster                                                        |
| asyncio_tcp             | 883 ms                                                 | 503 ms: 1.76x faster                                                         |
| json_dumps              | 12.4 ms                                                | 9.45 ms: 1.31x faster                                                        |
| mypy2                   | 420 ms                                                 | 332 ms: 1.26x faster                                                         |
| unpickle_pure_python    | 227 us                                                 | 195 us: 1.17x faster                                                         |
| deltablue               | 3.66 ms                                                | 3.16 ms: 1.16x faster                                                        |
| coroutines              | 26.2 ms                                                | 22.8 ms: 1.15x faster                                                        |
| genshi_xml              | 51.4 ms                                                | 46.5 ms: 1.11x faster                                                        |
| json_loads              | 26.1 us                                                | 23.6 us: 1.10x faster                                                        |
| scimark_sor             | 115 ms                                                 | 104 ms: 1.10x faster                                                         |
| richards                | 46.1 ms                                                | 42.0 ms: 1.10x faster                                                        |
| pickle_pure_python      | 308 us                                                 | 283 us: 1.09x faster                                                         |
| pycparser               | 1.19 sec                                               | 1.09 sec: 1.08x faster                                                       |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.23 ms: 1.08x faster                                                        |
| xml_etree_parse         | 160 ms                                                 | 149 ms: 1.08x faster                                                         |
| nqueens                 | 83.8 ms                                                | 78.2 ms: 1.07x faster                                                        |
| json                    | 4.87 ms                                                | 4.55 ms: 1.07x faster                                                        |
| hexiom                  | 6.34 ms                                                | 5.95 ms: 1.07x faster                                                        |
| regex_compile           | 136 ms                                                 | 129 ms: 1.06x faster                                                         |
| html5lib                | 64.8 ms                                                | 61.3 ms: 1.06x faster                                                        |
| float                   | 76.8 ms                                                | 72.6 ms: 1.06x faster                                                        |
| fannkuch                | 384 ms                                                 | 364 ms: 1.06x faster                                                         |
| logging_silent          | 98.0 ns                                                | 92.9 ns: 1.06x faster                                                        |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.06x faster                                                       |
| sympy_expand            | 475 ms                                                 | 453 ms: 1.05x faster                                                         |
| sqlglot_normalize       | 108 ms                                                 | 103 ms: 1.05x faster                                                         |
| 2to3                    | 259 ms                                                 | 247 ms: 1.05x faster                                                         |
| mdp                     | 2.63 sec                                               | 2.51 sec: 1.05x faster                                                       |
| xml_etree_iterparse     | 104 ms                                                 | 99.3 ms: 1.05x faster                                                        |
| sqlglot_optimize        | 52.7 ms                                                | 50.4 ms: 1.05x faster                                                        |
| pyflate                 | 419 ms                                                 | 400 ms: 1.05x faster                                                         |
| deepcopy_memo           | 35.8 us                                                | 34.2 us: 1.05x faster                                                        |
| pprint_safe_repr        | 706 ms                                                 | 676 ms: 1.04x faster                                                         |
| gc_traversal            | 3.82 ms                                                | 3.67 ms: 1.04x faster                                                        |
| aiohttp                 | 1.05 ms                                                | 1.01 ms: 1.04x faster                                                        |
| logging_simple          | 6.02 us                                                | 5.80 us: 1.04x faster                                                        |
| scimark_fft             | 325 ms                                                 | 314 ms: 1.04x faster                                                         |
| deepcopy                | 341 us                                                 | 329 us: 1.04x faster                                                         |
| go                      | 140 ms                                                 | 135 ms: 1.04x faster                                                         |
| crypto_pyaes            | 75.7 ms                                                | 73.1 ms: 1.04x faster                                                        |
| genshi_text             | 21.5 ms                                                | 20.8 ms: 1.03x faster                                                        |
| chaos                   | 68.7 ms                                                | 66.4 ms: 1.03x faster                                                        |
| unpack_sequence         | 44.5 ns                                                | 43.1 ns: 1.03x faster                                                        |
| bench_thread_pool       | 817 us                                                 | 792 us: 1.03x faster                                                         |
| deepcopy_reduce         | 3.02 us                                                | 2.93 us: 1.03x faster                                                        |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.03x faster                                                        |
| docutils                | 2.60 sec                                               | 2.53 sec: 1.03x faster                                                       |
| coverage                | 99.3 ms                                                | 96.4 ms: 1.03x faster                                                        |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                                        |
| regex_effbot            | 3.46 ms                                                | 3.36 ms: 1.03x faster                                                        |
| sympy_str               | 291 ms                                                 | 284 ms: 1.03x faster                                                         |
| raytrace                | 291 ms                                                 | 284 ms: 1.03x faster                                                         |
| create_gc_cycles        | 1.52 ms                                                | 1.48 ms: 1.02x faster                                                        |
| pidigits                | 197 ms                                                 | 192 ms: 1.02x faster                                                         |
| logging_format          | 6.48 us                                                | 6.33 us: 1.02x faster                                                        |
| scimark_monte_carlo     | 68.0 ms                                                | 66.5 ms: 1.02x faster                                                        |
| tornado_http            | 96.5 ms                                                | 94.7 ms: 1.02x faster                                                        |
| pathlib                 | 18.1 ms                                                | 17.7 ms: 1.02x faster                                                        |
| spectral_norm           | 98.1 ms                                                | 96.8 ms: 1.01x faster                                                        |
| sqlalchemy_imperative   | 18.1 ms                                                | 17.8 ms: 1.01x faster                                                        |
| dulwich_log             | 64.0 ms                                                | 63.3 ms: 1.01x faster                                                        |
| regex_v8                | 22.2 ms                                                | 22.1 ms: 1.01x faster                                                        |
| thrift                  | 760 us                                                 | 764 us: 1.01x slower                                                         |
| chameleon               | 6.38 ms                                                | 6.42 ms: 1.01x slower                                                        |
| telco                   | 6.43 ms                                                | 6.50 ms: 1.01x slower                                                        |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                                       |
| django_template         | 32.3 ms                                                | 32.9 ms: 1.02x slower                                                        |
| xml_etree_process       | 53.7 ms                                                | 54.6 ms: 1.02x slower                                                        |
| python_startup          | 8.58 ms                                                | 8.81 ms: 1.03x slower                                                        |
| regex_dna               | 203 ms                                                 | 210 ms: 1.03x slower                                                         |
| pickle_list             | 4.14 us                                                | 4.30 us: 1.04x slower                                                        |
| pickle                  | 9.90 us                                                | 10.3 us: 1.04x slower                                                        |
| pickle_dict             | 31.2 us                                                | 32.4 us: 1.04x slower                                                        |
| sqlglot_transpile       | 1.65 ms                                                | 1.72 ms: 1.04x slower                                                        |
| sqlglot_parse           | 1.36 ms                                                | 1.42 ms: 1.05x slower                                                        |
| python_startup_no_site  | 6.04 ms                                                | 6.34 ms: 1.05x slower                                                        |
| sqlite_synth            | 2.48 us                                                | 2.60 us: 1.05x slower                                                        |
| async_tree_memoization  | 624 ms                                                 | 656 ms: 1.05x slower                                                         |
| xml_etree_generate      | 75.9 ms                                                | 80.0 ms: 1.05x slower                                                        |
| nbody                   | 90.0 ms                                                | 96.0 ms: 1.07x slower                                                        |
| async_generators        | 356 ms                                                 | 408 ms: 1.15x slower                                                         |
| dask                    | 365 ms                                                 | 502 ms: 1.37x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (11): meteor_contest, sqlalchemy_declarative, mako, bench_mp_pool, sympy_sum, unpickle_list, async_tree_none, scimark_lu, async_tree_cpu_io_mixed, unpickle, djangocms
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint
