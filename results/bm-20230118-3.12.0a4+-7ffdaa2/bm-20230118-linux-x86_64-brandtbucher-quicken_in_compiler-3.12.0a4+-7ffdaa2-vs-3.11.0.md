
# Results vs. 3.11.0

- fork: brandtbucher
- ref: quicken_in_compiler
- machine: linux-x86_64
- commit hash: 7ffdaa2
- commit date: 2023-01-18
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 250 ms: 1.03x faster                                                        |
| chameleon      | 6.41 ms                                                | 6.28 ms: 1.02x faster                                                       |
| docutils       | 2.60 sec                                               | 2.52 sec: 1.03x faster                                                      |
| html5lib       | 63.2 ms                                                | 59.7 ms: 1.06x faster                                                       |
| tornado_http   | 96.6 ms                                                | 93.9 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 72.0 ms: 1.06x faster                                                       |
| nbody          | 95.0 ms                                                | 93.9 ms: 1.01x faster                                                       |
| pidigits       | 199 ms                                                 | 198 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.06x faster                                                        |
| regex_v8       | 22.3 ms                                                | 21.8 ms: 1.03x faster                                                       |
| regex_dna      | 203 ms                                                 | 208 ms: 1.02x slower                                                        |
| regex_effbot   | 3.36 ms                                                | 3.44 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.45 ms: 1.34x faster                                                       |
| unpickle_pure_python | 225 us                                                 | 196 us: 1.15x faster                                                        |
| json_loads           | 26.2 us                                                | 24.0 us: 1.09x faster                                                       |
| pickle_pure_python   | 304 us                                                 | 280 us: 1.08x faster                                                        |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.08x faster                                                        |
| pickle_list          | 4.17 us                                                | 4.04 us: 1.03x faster                                                       |
| pickle_dict          | 31.4 us                                                | 31.0 us: 1.01x faster                                                       |
| xml_etree_process    | 53.8 ms                                                | 54.0 ms: 1.00x slower                                                       |
| xml_etree_iterparse  | 103 ms                                                 | 105 ms: 1.02x slower                                                        |
| xml_etree_generate   | 76.2 ms                                                | 77.9 ms: 1.02x slower                                                       |
| pickle               | 9.79 us                                                | 10.1 us: 1.03x slower                                                       |
| unpickle_list        | 4.95 us                                                | 5.11 us: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.84 ms: 1.06x slower                                                       |
| python_startup_no_site | 5.96 ms                                                | 6.39 ms: 1.07x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml     | 52.1 ms                                                | 46.6 ms: 1.12x faster                                                       |
| genshi_text    | 22.1 ms                                                | 20.3 ms: 1.09x faster                                                       |
| mako           | 9.85 ms                                                | 9.75 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.45 ms: 1.34x faster                                                       |
| unpickle_pure_python    | 225 us                                                 | 196 us: 1.15x faster                                                        |
| scimark_sparse_mat_mult | 4.40 ms                                                | 3.93 ms: 1.12x faster                                                       |
| genshi_xml              | 52.1 ms                                                | 46.6 ms: 1.12x faster                                                       |
| nqueens                 | 85.0 ms                                                | 76.3 ms: 1.11x faster                                                       |
| deltablue               | 3.64 ms                                                | 3.28 ms: 1.11x faster                                                       |
| scimark_fft             | 329 ms                                                 | 296 ms: 1.11x faster                                                        |
| scimark_sor             | 115 ms                                                 | 104 ms: 1.11x faster                                                        |
| richards                | 46.2 ms                                                | 42.1 ms: 1.10x faster                                                       |
| json_loads              | 26.2 us                                                | 24.0 us: 1.09x faster                                                       |
| genshi_text             | 22.1 ms                                                | 20.3 ms: 1.09x faster                                                       |
| pickle_pure_python      | 304 us                                                 | 280 us: 1.08x faster                                                        |
| json                    | 4.95 ms                                                | 4.58 ms: 1.08x faster                                                       |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.08x faster                                                        |
| go                      | 143 ms                                                 | 134 ms: 1.07x faster                                                        |
| sympy_str               | 287 ms                                                 | 269 ms: 1.07x faster                                                        |
| logging_silent          | 98.5 ns                                                | 92.1 ns: 1.07x faster                                                       |
| pyflate                 | 417 ms                                                 | 391 ms: 1.07x faster                                                        |
| hexiom                  | 6.35 ms                                                | 5.95 ms: 1.07x faster                                                       |
| chaos                   | 68.6 ms                                                | 64.4 ms: 1.06x faster                                                       |
| sympy_sum               | 166 ms                                                 | 156 ms: 1.06x faster                                                        |
| float                   | 76.3 ms                                                | 72.0 ms: 1.06x faster                                                       |
| regex_compile           | 136 ms                                                 | 128 ms: 1.06x faster                                                        |
| sympy_integrate         | 20.9 ms                                                | 19.7 ms: 1.06x faster                                                       |
| coroutines              | 26.1 ms                                                | 24.6 ms: 1.06x faster                                                       |
| spectral_norm           | 99.9 ms                                                | 94.4 ms: 1.06x faster                                                       |
| html5lib                | 63.2 ms                                                | 59.7 ms: 1.06x faster                                                       |
| deepcopy_memo           | 36.4 us                                                | 34.5 us: 1.06x faster                                                       |
| coverage                | 101 ms                                                 | 95.3 ms: 1.05x faster                                                       |
| aiohttp                 | 1.05 ms                                                | 992 us: 1.05x faster                                                        |
| pycparser               | 1.17 sec                                               | 1.12 sec: 1.05x faster                                                      |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.05x faster                                                       |
| logging_simple          | 6.06 us                                                | 5.77 us: 1.05x faster                                                       |
| fannkuch                | 388 ms                                                 | 371 ms: 1.05x faster                                                        |
| sympy_expand            | 472 ms                                                 | 452 ms: 1.05x faster                                                        |
| sqlglot_optimize        | 53.0 ms                                                | 51.0 ms: 1.04x faster                                                       |
| telco                   | 6.62 ms                                                | 6.37 ms: 1.04x faster                                                       |
| logging_format          | 6.62 us                                                | 6.37 us: 1.04x faster                                                       |
| bench_thread_pool       | 810 us                                                 | 780 us: 1.04x faster                                                        |
| raytrace                | 290 ms                                                 | 280 ms: 1.04x faster                                                        |
| pathlib                 | 18.2 ms                                                | 17.5 ms: 1.04x faster                                                       |
| deepcopy                | 344 us                                                 | 332 us: 1.04x faster                                                        |
| scimark_monte_carlo     | 68.3 ms                                                | 66.0 ms: 1.03x faster                                                       |
| pickle_list             | 4.17 us                                                | 4.04 us: 1.03x faster                                                       |
| 2to3                    | 257 ms                                                 | 250 ms: 1.03x faster                                                        |
| docutils                | 2.60 sec                                               | 2.52 sec: 1.03x faster                                                      |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                        |
| tornado_http            | 96.6 ms                                                | 93.9 ms: 1.03x faster                                                       |
| dulwich_log             | 63.9 ms                                                | 62.1 ms: 1.03x faster                                                       |
| regex_v8                | 22.3 ms                                                | 21.8 ms: 1.03x faster                                                       |
| pprint_pformat          | 1.44 sec                                               | 1.41 sec: 1.03x faster                                                      |
| async_generators        | 359 ms                                                 | 351 ms: 1.02x faster                                                        |
| meteor_contest          | 105 ms                                                 | 103 ms: 1.02x faster                                                        |
| chameleon               | 6.41 ms                                                | 6.28 ms: 1.02x faster                                                       |
| pickle_dict             | 31.4 us                                                | 31.0 us: 1.01x faster                                                       |
| nbody                   | 95.0 ms                                                | 93.9 ms: 1.01x faster                                                       |
| mako                    | 9.85 ms                                                | 9.75 ms: 1.01x faster                                                       |
| pidigits                | 199 ms                                                 | 198 ms: 1.01x faster                                                        |
| crypto_pyaes            | 73.9 ms                                                | 73.2 ms: 1.01x faster                                                       |
| thrift                  | 752 us                                                 | 747 us: 1.01x faster                                                        |
| xml_etree_process       | 53.8 ms                                                | 54.0 ms: 1.00x slower                                                       |
| pprint_safe_repr        | 691 ms                                                 | 696 ms: 1.01x slower                                                        |
| async_tree_io           | 1.31 sec                                               | 1.32 sec: 1.01x slower                                                      |
| mdp                     | 2.62 sec                                               | 2.66 sec: 1.01x slower                                                      |
| xml_etree_iterparse     | 103 ms                                                 | 105 ms: 1.02x slower                                                        |
| sqlglot_transpile       | 1.66 ms                                                | 1.69 ms: 1.02x slower                                                       |
| unpack_sequence         | 43.4 ns                                                | 44.3 ns: 1.02x slower                                                       |
| xml_etree_generate      | 76.2 ms                                                | 77.9 ms: 1.02x slower                                                       |
| sqlglot_parse           | 1.37 ms                                                | 1.40 ms: 1.02x slower                                                       |
| regex_dna               | 203 ms                                                 | 208 ms: 1.02x slower                                                        |
| regex_effbot            | 3.36 ms                                                | 3.44 ms: 1.02x slower                                                       |
| pickle                  | 9.79 us                                                | 10.1 us: 1.03x slower                                                       |
| unpickle_list           | 4.95 us                                                | 5.11 us: 1.03x slower                                                       |
| sqlite_synth            | 2.49 us                                                | 2.57 us: 1.03x slower                                                       |
| generators              | 72.2 ms                                                | 75.0 ms: 1.04x slower                                                       |
| async_tree_memoization  | 625 ms                                                 | 653 ms: 1.04x slower                                                        |
| python_startup          | 8.36 ms                                                | 8.84 ms: 1.06x slower                                                       |
| python_startup_no_site  | 5.96 ms                                                | 6.39 ms: 1.07x slower                                                       |
| mypy                    | 669 ms                                                 | 805 ms: 1.20x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                                |

Benchmark hidden because not significant (7): async_tree_none, deepcopy_reduce, scimark_lu, bench_mp_pool, unpickle, django_template, async_tree_cpu_io_mixed
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230118-3.12.0a4+-7ffdaa2/bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
