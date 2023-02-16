
# Results vs. 3.11.0

- fork: brandtbucher
- ref: quicken_in_compiler
- machine: linux-x86_64
- commit hash: 7ffdaa2
- commit date: 2023-01-18
- overall geometric mean: 1.04x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 250 ms: 1.04x faster                                                        |
| chameleon      | 6.38 ms                                                | 6.28 ms: 1.02x faster                                                       |
| docutils       | 2.60 sec                                               | 2.52 sec: 1.03x faster                                                      |
| html5lib       | 64.8 ms                                                | 59.7 ms: 1.08x faster                                                       |
| tornado_http   | 96.5 ms                                                | 93.9 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.0 ms: 1.07x faster                                                       |
| pidigits       | 197 ms                                                 | 198 ms: 1.00x slower                                                        |
| nbody          | 90.0 ms                                                | 93.9 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.06x faster                                                        |
| regex_v8       | 22.2 ms                                                | 21.8 ms: 1.02x faster                                                       |
| regex_dna      | 203 ms                                                 | 208 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.45 ms: 1.31x faster                                                       |
| unpickle_pure_python | 227 us                                                 | 196 us: 1.16x faster                                                        |
| pickle_pure_python   | 308 us                                                 | 280 us: 1.10x faster                                                        |
| xml_etree_parse      | 160 ms                                                 | 147 ms: 1.09x faster                                                        |
| json_loads           | 26.1 us                                                | 24.0 us: 1.08x faster                                                       |
| pickle_list          | 4.14 us                                                | 4.04 us: 1.02x faster                                                       |
| pickle_dict          | 31.2 us                                                | 31.0 us: 1.01x faster                                                       |
| xml_etree_process    | 53.7 ms                                                | 54.0 ms: 1.01x slower                                                       |
| pickle               | 9.90 us                                                | 10.1 us: 1.02x slower                                                       |
| unpickle_list        | 4.99 us                                                | 5.11 us: 1.02x slower                                                       |
| xml_etree_generate   | 75.9 ms                                                | 77.9 ms: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                |

Benchmark hidden because not significant (2): unpickle, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.84 ms: 1.03x slower                                                       |
| python_startup_no_site | 6.04 ms                                                | 6.39 ms: 1.06x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 46.6 ms: 1.10x faster                                                       |
| genshi_text     | 21.5 ms                                                | 20.3 ms: 1.06x faster                                                       |
| mako            | 9.83 ms                                                | 9.75 ms: 1.01x faster                                                       |
| django_template | 32.3 ms                                                | 32.5 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 489 ms: 1.81x faster                                                        |
| json_dumps              | 12.4 ms                                                | 9.45 ms: 1.31x faster                                                       |
| scimark_sparse_mat_mult | 4.59 ms                                                | 3.93 ms: 1.17x faster                                                       |
| unpickle_pure_python    | 227 us                                                 | 196 us: 1.16x faster                                                        |
| deltablue               | 3.66 ms                                                | 3.28 ms: 1.12x faster                                                       |
| genshi_xml              | 51.4 ms                                                | 46.6 ms: 1.10x faster                                                       |
| scimark_sor             | 115 ms                                                 | 104 ms: 1.10x faster                                                        |
| scimark_fft             | 325 ms                                                 | 296 ms: 1.10x faster                                                        |
| pickle_pure_python      | 308 us                                                 | 280 us: 1.10x faster                                                        |
| nqueens                 | 83.8 ms                                                | 76.3 ms: 1.10x faster                                                       |
| richards                | 46.1 ms                                                | 42.1 ms: 1.09x faster                                                       |
| xml_etree_parse         | 160 ms                                                 | 147 ms: 1.09x faster                                                        |
| json_loads              | 26.1 us                                                | 24.0 us: 1.08x faster                                                       |
| html5lib                | 64.8 ms                                                | 59.7 ms: 1.08x faster                                                       |
| sympy_str               | 291 ms                                                 | 269 ms: 1.08x faster                                                        |
| pyflate                 | 419 ms                                                 | 391 ms: 1.07x faster                                                        |
| float                   | 76.8 ms                                                | 72.0 ms: 1.07x faster                                                       |
| chaos                   | 68.7 ms                                                | 64.4 ms: 1.07x faster                                                       |
| hexiom                  | 6.34 ms                                                | 5.95 ms: 1.06x faster                                                       |
| logging_silent          | 98.0 ns                                                | 92.1 ns: 1.06x faster                                                       |
| sympy_sum               | 166 ms                                                 | 156 ms: 1.06x faster                                                        |
| pycparser               | 1.19 sec                                               | 1.12 sec: 1.06x faster                                                      |
| sympy_integrate         | 21.0 ms                                                | 19.7 ms: 1.06x faster                                                       |
| json                    | 4.87 ms                                                | 4.58 ms: 1.06x faster                                                       |
| regex_compile           | 136 ms                                                 | 128 ms: 1.06x faster                                                        |
| coroutines              | 26.2 ms                                                | 24.6 ms: 1.06x faster                                                       |
| genshi_text             | 21.5 ms                                                | 20.3 ms: 1.06x faster                                                       |
| aiohttp                 | 1.05 ms                                                | 992 us: 1.06x faster                                                        |
| sympy_expand            | 475 ms                                                 | 452 ms: 1.05x faster                                                        |
| create_gc_cycles        | 1.52 ms                                                | 1.44 ms: 1.05x faster                                                       |
| go                      | 140 ms                                                 | 134 ms: 1.05x faster                                                        |
| bench_thread_pool       | 817 us                                                 | 780 us: 1.05x faster                                                        |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.05x faster                                                       |
| logging_simple          | 6.02 us                                                | 5.77 us: 1.04x faster                                                       |
| raytrace                | 291 ms                                                 | 280 ms: 1.04x faster                                                        |
| coverage                | 99.3 ms                                                | 95.3 ms: 1.04x faster                                                       |
| 2to3                    | 259 ms                                                 | 250 ms: 1.04x faster                                                        |
| spectral_norm           | 98.1 ms                                                | 94.4 ms: 1.04x faster                                                       |
| deepcopy_memo           | 35.8 us                                                | 34.5 us: 1.04x faster                                                       |
| fannkuch                | 384 ms                                                 | 371 ms: 1.04x faster                                                        |
| pprint_pformat          | 1.46 sec                                               | 1.41 sec: 1.03x faster                                                      |
| sqlglot_optimize        | 52.7 ms                                                | 51.0 ms: 1.03x faster                                                       |
| crypto_pyaes            | 75.7 ms                                                | 73.2 ms: 1.03x faster                                                       |
| docutils                | 2.60 sec                                               | 2.52 sec: 1.03x faster                                                      |
| pathlib                 | 18.1 ms                                                | 17.5 ms: 1.03x faster                                                       |
| dulwich_log             | 64.0 ms                                                | 62.1 ms: 1.03x faster                                                       |
| scimark_monte_carlo     | 68.0 ms                                                | 66.0 ms: 1.03x faster                                                       |
| deepcopy                | 341 us                                                 | 332 us: 1.03x faster                                                        |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                        |
| tornado_http            | 96.5 ms                                                | 93.9 ms: 1.03x faster                                                       |
| pickle_list             | 4.14 us                                                | 4.04 us: 1.02x faster                                                       |
| regex_v8                | 22.2 ms                                                | 21.8 ms: 1.02x faster                                                       |
| deepcopy_reduce         | 3.02 us                                                | 2.96 us: 1.02x faster                                                       |
| meteor_contest          | 104 ms                                                 | 103 ms: 1.02x faster                                                        |
| thrift                  | 760 us                                                 | 747 us: 1.02x faster                                                        |
| logging_format          | 6.48 us                                                | 6.37 us: 1.02x faster                                                       |
| chameleon               | 6.38 ms                                                | 6.28 ms: 1.02x faster                                                       |
| pprint_safe_repr        | 706 ms                                                 | 696 ms: 1.01x faster                                                        |
| async_generators        | 356 ms                                                 | 351 ms: 1.01x faster                                                        |
| mako                    | 9.83 ms                                                | 9.75 ms: 1.01x faster                                                       |
| telco                   | 6.43 ms                                                | 6.37 ms: 1.01x faster                                                       |
| pickle_dict             | 31.2 us                                                | 31.0 us: 1.01x faster                                                       |
| gc_traversal            | 3.82 ms                                                | 3.81 ms: 1.00x faster                                                       |
| pidigits                | 197 ms                                                 | 198 ms: 1.00x slower                                                        |
| django_template         | 32.3 ms                                                | 32.5 ms: 1.01x slower                                                       |
| xml_etree_process       | 53.7 ms                                                | 54.0 ms: 1.01x slower                                                       |
| mdp                     | 2.63 sec                                               | 2.66 sec: 1.01x slower                                                      |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                                      |
| pickle                  | 9.90 us                                                | 10.1 us: 1.02x slower                                                       |
| generators              | 73.5 ms                                                | 75.0 ms: 1.02x slower                                                       |
| regex_dna               | 203 ms                                                 | 208 ms: 1.02x slower                                                        |
| unpickle_list           | 4.99 us                                                | 5.11 us: 1.02x slower                                                       |
| sqlglot_transpile       | 1.65 ms                                                | 1.69 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed | 736 ms                                                 | 755 ms: 1.03x slower                                                        |
| xml_etree_generate      | 75.9 ms                                                | 77.9 ms: 1.03x slower                                                       |
| sqlglot_parse           | 1.36 ms                                                | 1.40 ms: 1.03x slower                                                       |
| python_startup          | 8.58 ms                                                | 8.84 ms: 1.03x slower                                                       |
| sqlite_synth            | 2.48 us                                                | 2.57 us: 1.04x slower                                                       |
| nbody                   | 90.0 ms                                                | 93.9 ms: 1.04x slower                                                       |
| async_tree_memoization  | 624 ms                                                 | 653 ms: 1.05x slower                                                        |
| python_startup_no_site  | 6.04 ms                                                | 6.39 ms: 1.06x slower                                                       |
| dask                    | 365 ms                                                 | 492 ms: 1.35x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                                |

Benchmark hidden because not significant (8): scimark_lu, regex_effbot, unpack_sequence, async_tree_none, djangocms, bench_mp_pool, unpickle, xml_etree_iterparse
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230118-3.12.0a4+-7ffdaa2/bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2.json: mypy
