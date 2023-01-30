
# Results vs. 3.11.0

- fork: brandtbucher
- ref: quicken_in_compiler
- machine: linux-x86_64
- commit hash: afbac86
- commit date: 2023-01-17
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 252 ms: 1.02x faster                                                        |
| docutils       | 2.60 sec                                               | 2.50 sec: 1.04x faster                                                      |
| html5lib       | 63.2 ms                                                | 60.3 ms: 1.05x faster                                                       |
| tornado_http   | 96.6 ms                                                | 93.8 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                 | 189 ms: 1.05x faster                                                        |
| float          | 76.3 ms                                                | 73.0 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 129 ms: 1.05x faster                                                        |
| regex_v8       | 22.3 ms                                                | 22.4 ms: 1.01x slower                                                       |
| regex_dna      | 203 ms                                                 | 207 ms: 1.02x slower                                                        |
| regex_effbot   | 3.36 ms                                                | 3.48 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.35 ms: 1.35x faster                                                       |
| unpickle_pure_python | 225 us                                                 | 204 us: 1.11x faster                                                        |
| json_loads           | 26.2 us                                                | 24.1 us: 1.09x faster                                                       |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.06x faster                                                        |
| pickle_pure_python   | 304 us                                                 | 288 us: 1.05x faster                                                        |
| pickle_dict          | 31.4 us                                                | 29.9 us: 1.05x faster                                                       |
| pickle_list          | 4.17 us                                                | 4.00 us: 1.04x faster                                                       |
| xml_etree_process    | 53.8 ms                                                | 54.4 ms: 1.01x slower                                                       |
| pickle               | 9.79 us                                                | 9.93 us: 1.01x slower                                                       |
| unpickle_list        | 4.95 us                                                | 5.06 us: 1.02x slower                                                       |
| xml_etree_generate   | 76.2 ms                                                | 78.0 ms: 1.02x slower                                                       |
| xml_etree_iterparse  | 103 ms                                                 | 106 ms: 1.04x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.89 ms: 1.06x slower                                                       |
| python_startup_no_site | 5.96 ms                                                | 6.42 ms: 1.08x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                | 47.4 ms: 1.10x faster                                                       |
| genshi_text     | 22.1 ms                                                | 20.9 ms: 1.06x faster                                                       |
| mako            | 9.85 ms                                                | 9.65 ms: 1.02x faster                                                       |
| django_template | 32.5 ms                                                | 32.0 ms: 1.01x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.35 ms: 1.35x faster                                                       |
| deltablue               | 3.64 ms                                                | 3.22 ms: 1.13x faster                                                       |
| nqueens                 | 85.0 ms                                                | 76.6 ms: 1.11x faster                                                       |
| unpickle_pure_python    | 225 us                                                 | 204 us: 1.11x faster                                                        |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.00 ms: 1.10x faster                                                       |
| genshi_xml              | 52.1 ms                                                | 47.4 ms: 1.10x faster                                                       |
| json_loads              | 26.2 us                                                | 24.1 us: 1.09x faster                                                       |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.08x faster                                                        |
| logging_silent          | 98.5 ns                                                | 91.2 ns: 1.08x faster                                                       |
| coverage                | 101 ms                                                 | 93.1 ms: 1.08x faster                                                       |
| scimark_fft             | 329 ms                                                 | 306 ms: 1.07x faster                                                        |
| richards                | 46.2 ms                                                | 43.0 ms: 1.07x faster                                                       |
| sympy_str               | 287 ms                                                 | 269 ms: 1.07x faster                                                        |
| chaos                   | 68.6 ms                                                | 64.3 ms: 1.07x faster                                                       |
| sympy_sum               | 166 ms                                                 | 155 ms: 1.07x faster                                                        |
| spectral_norm           | 99.9 ms                                                | 93.8 ms: 1.07x faster                                                       |
| hexiom                  | 6.35 ms                                                | 5.98 ms: 1.06x faster                                                       |
| json                    | 4.95 ms                                                | 4.66 ms: 1.06x faster                                                       |
| genshi_text             | 22.1 ms                                                | 20.9 ms: 1.06x faster                                                       |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.06x faster                                                        |
| deepcopy_memo           | 36.4 us                                                | 34.5 us: 1.06x faster                                                       |
| regex_compile           | 136 ms                                                 | 129 ms: 1.05x faster                                                        |
| pidigits                | 199 ms                                                 | 189 ms: 1.05x faster                                                        |
| pickle_pure_python      | 304 us                                                 | 288 us: 1.05x faster                                                        |
| sympy_integrate         | 20.9 ms                                                | 19.8 ms: 1.05x faster                                                       |
| pickle_dict             | 31.4 us                                                | 29.9 us: 1.05x faster                                                       |
| coroutines              | 26.1 ms                                                | 24.8 ms: 1.05x faster                                                       |
| html5lib                | 63.2 ms                                                | 60.3 ms: 1.05x faster                                                       |
| scimark_monte_carlo     | 68.3 ms                                                | 65.2 ms: 1.05x faster                                                       |
| deepcopy                | 344 us                                                 | 328 us: 1.05x faster                                                        |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.05x faster                                                       |
| unpack_sequence         | 43.4 ns                                                | 41.4 ns: 1.05x faster                                                       |
| float                   | 76.3 ms                                                | 73.0 ms: 1.05x faster                                                       |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.05x faster                                                       |
| pickle_list             | 4.17 us                                                | 4.00 us: 1.04x faster                                                       |
| pprint_pformat          | 1.44 sec                                               | 1.38 sec: 1.04x faster                                                      |
| telco                   | 6.62 ms                                                | 6.35 ms: 1.04x faster                                                       |
| logging_simple          | 6.06 us                                                | 5.82 us: 1.04x faster                                                       |
| go                      | 143 ms                                                 | 138 ms: 1.04x faster                                                        |
| bench_thread_pool       | 810 us                                                 | 778 us: 1.04x faster                                                        |
| sqlglot_optimize        | 53.0 ms                                                | 51.0 ms: 1.04x faster                                                       |
| docutils                | 2.60 sec                                               | 2.50 sec: 1.04x faster                                                      |
| sympy_expand            | 472 ms                                                 | 454 ms: 1.04x faster                                                        |
| pyflate                 | 417 ms                                                 | 404 ms: 1.03x faster                                                        |
| fannkuch                | 388 ms                                                 | 376 ms: 1.03x faster                                                        |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                        |
| tornado_http            | 96.6 ms                                                | 93.8 ms: 1.03x faster                                                       |
| pprint_safe_repr        | 691 ms                                                 | 671 ms: 1.03x faster                                                        |
| dulwich_log             | 63.9 ms                                                | 62.2 ms: 1.03x faster                                                       |
| logging_format          | 6.62 us                                                | 6.45 us: 1.03x faster                                                       |
| pathlib                 | 18.2 ms                                                | 17.7 ms: 1.02x faster                                                       |
| mdp                     | 2.62 sec                                               | 2.56 sec: 1.02x faster                                                      |
| 2to3                    | 257 ms                                                 | 252 ms: 1.02x faster                                                        |
| raytrace                | 290 ms                                                 | 284 ms: 1.02x faster                                                        |
| mako                    | 9.85 ms                                                | 9.65 ms: 1.02x faster                                                       |
| pycparser               | 1.17 sec                                               | 1.15 sec: 1.02x faster                                                      |
| thrift                  | 752 us                                                 | 739 us: 1.02x faster                                                        |
| async_generators        | 359 ms                                                 | 354 ms: 1.01x faster                                                        |
| django_template         | 32.5 ms                                                | 32.0 ms: 1.01x faster                                                       |
| crypto_pyaes            | 73.9 ms                                                | 73.2 ms: 1.01x faster                                                       |
| deepcopy_reduce         | 2.97 us                                                | 2.95 us: 1.01x faster                                                       |
| regex_v8                | 22.3 ms                                                | 22.4 ms: 1.01x slower                                                       |
| xml_etree_process       | 53.8 ms                                                | 54.4 ms: 1.01x slower                                                       |
| async_tree_io           | 1.31 sec                                               | 1.32 sec: 1.01x slower                                                      |
| pickle                  | 9.79 us                                                | 9.93 us: 1.01x slower                                                       |
| regex_dna               | 203 ms                                                 | 207 ms: 1.02x slower                                                        |
| unpickle_list           | 4.95 us                                                | 5.06 us: 1.02x slower                                                       |
| sqlglot_transpile       | 1.66 ms                                                | 1.70 ms: 1.02x slower                                                       |
| sqlglot_parse           | 1.37 ms                                                | 1.40 ms: 1.02x slower                                                       |
| xml_etree_generate      | 76.2 ms                                                | 78.0 ms: 1.02x slower                                                       |
| sqlite_synth            | 2.49 us                                                | 2.56 us: 1.03x slower                                                       |
| regex_effbot            | 3.36 ms                                                | 3.48 ms: 1.04x slower                                                       |
| xml_etree_iterparse     | 103 ms                                                 | 106 ms: 1.04x slower                                                        |
| async_tree_memoization  | 625 ms                                                 | 659 ms: 1.06x slower                                                        |
| generators              | 72.2 ms                                                | 76.6 ms: 1.06x slower                                                       |
| python_startup          | 8.36 ms                                                | 8.89 ms: 1.06x slower                                                       |
| python_startup_no_site  | 5.96 ms                                                | 6.42 ms: 1.08x slower                                                       |
| mypy                    | 669 ms                                                 | 805 ms: 1.20x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                                |

Benchmark hidden because not significant (8): async_tree_none, nbody, unpickle, scimark_lu, meteor_contest, chameleon, bench_mp_pool, async_tree_cpu_io_mixed
Ignored benchmarks (4) of /home/mdboom/Work/builds/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230117-3.12.0a4+-afbac86/bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
