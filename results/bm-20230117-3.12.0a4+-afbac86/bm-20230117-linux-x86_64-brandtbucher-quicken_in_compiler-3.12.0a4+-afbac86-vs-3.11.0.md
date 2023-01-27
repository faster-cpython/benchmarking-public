
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
| 2to3           | 257 ms                                                 | 251 ms: 1.03x faster                                                        |
| docutils       | 2.60 sec                                               | 2.48 sec: 1.04x faster                                                      |
| html5lib       | 63.2 ms                                                | 59.9 ms: 1.05x faster                                                       |
| tornado_http   | 96.6 ms                                                | 94.3 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 72.0 ms: 1.06x faster                                                       |
| nbody          | 95.0 ms                                                | 94.1 ms: 1.01x faster                                                       |
| pidigits       | 199 ms                                                 | 197 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.06x faster                                                        |
| regex_dna      | 203 ms                                                 | 210 ms: 1.03x slower                                                        |
| regex_effbot   | 3.36 ms                                                | 3.52 ms: 1.05x slower                                                       |
| regex_v8       | 22.3 ms                                                | 22.5 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.36 ms: 1.35x faster                                                       |
| json_loads           | 26.2 us                                                | 23.8 us: 1.10x faster                                                       |
| pickle               | 9.79 us                                                | 10.1 us: 1.03x slower                                                       |
| pickle_dict          | 31.4 us                                                | 30.9 us: 1.02x faster                                                       |
| pickle_list          | 4.17 us                                                | 4.10 us: 1.02x faster                                                       |
| pickle_pure_python   | 304 us                                                 | 288 us: 1.06x faster                                                        |
| unpickle_list        | 4.95 us                                                | 5.24 us: 1.06x slower                                                       |
| unpickle_pure_python | 225 us                                                 | 201 us: 1.12x faster                                                        |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                 | 102 ms: 1.01x faster                                                        |
| xml_etree_generate   | 76.2 ms                                                | 77.2 ms: 1.01x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                |

Benchmark hidden because not significant (2): unpickle, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.84 ms: 1.06x slower                                                       |
| python_startup_no_site | 5.96 ms                                                | 6.39 ms: 1.07x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text    | 22.1 ms                                                | 21.1 ms: 1.05x faster                                                       |
| genshi_xml     | 52.1 ms                                                | 47.3 ms: 1.10x faster                                                       |
| mako           | 9.85 ms                                                | 9.75 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3                    | 257 ms                                                 | 251 ms: 1.03x faster                                                        |
| aiohttp                 | 1.05 ms                                                | 993 us: 1.05x faster                                                        |
| async_generators        | 359 ms                                                 | 351 ms: 1.02x faster                                                        |
| async_tree_none         | 529 ms                                                 | 520 ms: 1.02x faster                                                        |
| async_tree_memoization  | 625 ms                                                 | 646 ms: 1.03x slower                                                        |
| chaos                   | 68.6 ms                                                | 64.2 ms: 1.07x faster                                                       |
| bench_thread_pool       | 810 us                                                 | 778 us: 1.04x faster                                                        |
| coroutines              | 26.1 ms                                                | 24.5 ms: 1.06x faster                                                       |
| coverage                | 101 ms                                                 | 93.5 ms: 1.08x faster                                                       |
| crypto_pyaes            | 73.9 ms                                                | 72.2 ms: 1.02x faster                                                       |
| deepcopy                | 344 us                                                 | 328 us: 1.05x faster                                                        |
| deepcopy_reduce         | 2.97 us                                                | 2.93 us: 1.01x faster                                                       |
| deepcopy_memo           | 36.4 us                                                | 34.4 us: 1.06x faster                                                       |
| deltablue               | 3.64 ms                                                | 3.23 ms: 1.13x faster                                                       |
| docutils                | 2.60 sec                                               | 2.48 sec: 1.04x faster                                                      |
| dulwich_log             | 63.9 ms                                                | 62.4 ms: 1.02x faster                                                       |
| fannkuch                | 388 ms                                                 | 366 ms: 1.06x faster                                                        |
| float                   | 76.3 ms                                                | 72.0 ms: 1.06x faster                                                       |
| generators              | 72.2 ms                                                | 77.0 ms: 1.07x slower                                                       |
| genshi_text             | 22.1 ms                                                | 21.1 ms: 1.05x faster                                                       |
| genshi_xml              | 52.1 ms                                                | 47.3 ms: 1.10x faster                                                       |
| go                      | 143 ms                                                 | 135 ms: 1.06x faster                                                        |
| gunicorn                | 1.12 ms                                                | 1.06 ms: 1.06x faster                                                       |
| hexiom                  | 6.35 ms                                                | 6.13 ms: 1.04x faster                                                       |
| html5lib                | 63.2 ms                                                | 59.9 ms: 1.05x faster                                                       |
| json                    | 4.95 ms                                                | 4.55 ms: 1.09x faster                                                       |
| json_dumps              | 12.7 ms                                                | 9.36 ms: 1.35x faster                                                       |
| json_loads              | 26.2 us                                                | 23.8 us: 1.10x faster                                                       |
| logging_format          | 6.62 us                                                | 6.42 us: 1.03x faster                                                       |
| logging_silent          | 98.5 ns                                                | 90.1 ns: 1.09x faster                                                       |
| logging_simple          | 6.06 us                                                | 5.83 us: 1.04x faster                                                       |
| mako                    | 9.85 ms                                                | 9.75 ms: 1.01x faster                                                       |
| mdp                     | 2.62 sec                                               | 2.61 sec: 1.01x faster                                                      |
| mypy                    | 669 ms                                                 | 802 ms: 1.20x slower                                                        |
| nbody                   | 95.0 ms                                                | 94.1 ms: 1.01x faster                                                       |
| nqueens                 | 85.0 ms                                                | 76.3 ms: 1.11x faster                                                       |
| pathlib                 | 18.2 ms                                                | 17.9 ms: 1.02x faster                                                       |
| pickle                  | 9.79 us                                                | 10.1 us: 1.03x slower                                                       |
| pickle_dict             | 31.4 us                                                | 30.9 us: 1.02x faster                                                       |
| pickle_list             | 4.17 us                                                | 4.10 us: 1.02x faster                                                       |
| pickle_pure_python      | 304 us                                                 | 288 us: 1.06x faster                                                        |
| pidigits                | 199 ms                                                 | 197 ms: 1.01x faster                                                        |
| pprint_safe_repr        | 691 ms                                                 | 677 ms: 1.02x faster                                                        |
| pprint_pformat          | 1.44 sec                                               | 1.38 sec: 1.04x faster                                                      |
| pycparser               | 1.17 sec                                               | 1.14 sec: 1.03x faster                                                      |
| pyflate                 | 417 ms                                                 | 414 ms: 1.01x faster                                                        |
| python_startup          | 8.36 ms                                                | 8.84 ms: 1.06x slower                                                       |
| python_startup_no_site  | 5.96 ms                                                | 6.39 ms: 1.07x slower                                                       |
| raytrace                | 290 ms                                                 | 284 ms: 1.02x faster                                                        |
| regex_compile           | 136 ms                                                 | 128 ms: 1.06x faster                                                        |
| regex_dna               | 203 ms                                                 | 210 ms: 1.03x slower                                                        |
| regex_effbot            | 3.36 ms                                                | 3.52 ms: 1.05x slower                                                       |
| regex_v8                | 22.3 ms                                                | 22.5 ms: 1.01x slower                                                       |
| richards                | 46.2 ms                                                | 42.4 ms: 1.09x faster                                                       |
| scimark_fft             | 329 ms                                                 | 302 ms: 1.09x faster                                                        |
| scimark_monte_carlo     | 68.3 ms                                                | 66.1 ms: 1.03x faster                                                       |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.09x faster                                                        |
| scimark_sparse_mat_mult | 4.40 ms                                                | 3.98 ms: 1.10x faster                                                       |
| spectral_norm           | 99.9 ms                                                | 94.5 ms: 1.06x faster                                                       |
| sqlglot_parse           | 1.37 ms                                                | 1.41 ms: 1.03x slower                                                       |
| sqlglot_transpile       | 1.66 ms                                                | 1.70 ms: 1.02x slower                                                       |
| sqlglot_optimize        | 53.0 ms                                                | 51.0 ms: 1.04x faster                                                       |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                        |
| sqlite_synth            | 2.49 us                                                | 2.59 us: 1.04x slower                                                       |
| sympy_expand            | 472 ms                                                 | 454 ms: 1.04x faster                                                        |
| sympy_integrate         | 20.9 ms                                                | 19.7 ms: 1.06x faster                                                       |
| sympy_sum               | 166 ms                                                 | 155 ms: 1.07x faster                                                        |
| sympy_str               | 287 ms                                                 | 270 ms: 1.06x faster                                                        |
| telco                   | 6.62 ms                                                | 6.45 ms: 1.03x faster                                                       |
| thrift                  | 752 us                                                 | 737 us: 1.02x faster                                                        |
| tornado_http            | 96.6 ms                                                | 94.3 ms: 1.02x faster                                                       |
| unpickle_list           | 4.95 us                                                | 5.24 us: 1.06x slower                                                       |
| unpickle_pure_python    | 225 us                                                 | 201 us: 1.12x faster                                                        |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                        |
| xml_etree_iterparse     | 103 ms                                                 | 102 ms: 1.01x faster                                                        |
| xml_etree_generate      | 76.2 ms                                                | 77.2 ms: 1.01x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                                |

Benchmark hidden because not significant (10): async_tree_cpu_io_mixed, async_tree_io, chameleon, bench_mp_pool, django_template, meteor_contest, scimark_lu, unpack_sequence, unpickle, xml_etree_process
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230117-3.12.0a4+-afbac86/bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
