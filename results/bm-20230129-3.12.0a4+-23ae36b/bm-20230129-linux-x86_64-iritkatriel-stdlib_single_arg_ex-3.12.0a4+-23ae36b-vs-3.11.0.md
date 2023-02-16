
# Results vs. 3.11.0

- fork: iritkatriel
- ref: stdlib_single_arg_ex
- machine: linux-x86_64
- commit hash: 23ae36b
- commit date: 2023-01-29
- overall geometric mean: 1.04x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                                        |
| docutils       | 2.60 sec                                               | 2.48 sec: 1.05x faster                                                      |
| html5lib       | 64.8 ms                                                | 59.6 ms: 1.09x faster                                                       |
| tornado_http   | 96.5 ms                                                | 93.8 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 73.8 ms: 1.04x faster                                                       |
| pidigits       | 197 ms                                                 | 193 ms: 1.02x faster                                                        |
| nbody          | 90.0 ms                                                | 95.6 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.07x faster                                                        |
| regex_v8       | 22.2 ms                                                | 21.0 ms: 1.06x faster                                                       |
| regex_effbot   | 3.46 ms                                                | 3.38 ms: 1.02x faster                                                       |
| regex_dna      | 203 ms                                                 | 202 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.36 ms: 1.32x faster                                                       |
| unpickle_pure_python | 227 us                                                 | 199 us: 1.14x faster                                                        |
| xml_etree_parse      | 160 ms                                                 | 147 ms: 1.09x faster                                                        |
| pickle_pure_python   | 308 us                                                 | 283 us: 1.09x faster                                                        |
| json_loads           | 26.1 us                                                | 24.0 us: 1.08x faster                                                       |
| unpickle             | 13.3 us                                                | 13.0 us: 1.02x faster                                                       |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                        |
| unpickle_list        | 4.99 us                                                | 4.94 us: 1.01x faster                                                       |
| xml_etree_process    | 53.7 ms                                                | 53.2 ms: 1.01x faster                                                       |
| pickle_dict          | 31.2 us                                                | 31.0 us: 1.01x faster                                                       |
| xml_etree_generate   | 75.9 ms                                                | 77.1 ms: 1.02x slower                                                       |
| pickle_list          | 4.14 us                                                | 4.22 us: 1.02x slower                                                       |
| pickle               | 9.90 us                                                | 10.2 us: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.93 ms: 1.04x slower                                                       |
| python_startup_no_site | 6.04 ms                                                | 6.46 ms: 1.07x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml     | 51.4 ms                                                | 47.5 ms: 1.08x faster                                                       |
| genshi_text    | 21.5 ms                                                | 20.3 ms: 1.06x faster                                                       |
| mako           | 9.83 ms                                                | 9.85 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 495 ms: 1.78x faster                                                        |
| json_dumps              | 12.4 ms                                                | 9.36 ms: 1.32x faster                                                       |
| deltablue               | 3.66 ms                                                | 3.20 ms: 1.14x faster                                                       |
| unpickle_pure_python    | 227 us                                                 | 199 us: 1.14x faster                                                        |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.06 ms: 1.13x faster                                                       |
| richards                | 46.1 ms                                                | 41.9 ms: 1.10x faster                                                       |
| pycparser               | 1.19 sec                                               | 1.08 sec: 1.10x faster                                                      |
| xml_etree_parse         | 160 ms                                                 | 147 ms: 1.09x faster                                                        |
| pickle_pure_python      | 308 us                                                 | 283 us: 1.09x faster                                                        |
| logging_silent          | 98.0 ns                                                | 90.0 ns: 1.09x faster                                                       |
| html5lib                | 64.8 ms                                                | 59.6 ms: 1.09x faster                                                       |
| json_loads              | 26.1 us                                                | 24.0 us: 1.08x faster                                                       |
| genshi_xml              | 51.4 ms                                                | 47.5 ms: 1.08x faster                                                       |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.08x faster                                                        |
| hexiom                  | 6.34 ms                                                | 5.86 ms: 1.08x faster                                                       |
| sympy_str               | 291 ms                                                 | 269 ms: 1.08x faster                                                        |
| fannkuch                | 384 ms                                                 | 358 ms: 1.07x faster                                                        |
| bench_thread_pool       | 817 us                                                 | 761 us: 1.07x faster                                                        |
| regex_compile           | 136 ms                                                 | 128 ms: 1.07x faster                                                        |
| pprint_pformat          | 1.46 sec                                               | 1.36 sec: 1.07x faster                                                      |
| scimark_fft             | 325 ms                                                 | 305 ms: 1.07x faster                                                        |
| sympy_sum               | 166 ms                                                 | 156 ms: 1.06x faster                                                        |
| chaos                   | 68.7 ms                                                | 64.5 ms: 1.06x faster                                                       |
| json                    | 4.87 ms                                                | 4.58 ms: 1.06x faster                                                       |
| sympy_integrate         | 21.0 ms                                                | 19.7 ms: 1.06x faster                                                       |
| genshi_text             | 21.5 ms                                                | 20.3 ms: 1.06x faster                                                       |
| nqueens                 | 83.8 ms                                                | 79.1 ms: 1.06x faster                                                       |
| regex_v8                | 22.2 ms                                                | 21.0 ms: 1.06x faster                                                       |
| aiohttp                 | 1.05 ms                                                | 992 us: 1.06x faster                                                        |
| sympy_expand            | 475 ms                                                 | 451 ms: 1.05x faster                                                        |
| pprint_safe_repr        | 706 ms                                                 | 670 ms: 1.05x faster                                                        |
| logging_simple          | 6.02 us                                                | 5.72 us: 1.05x faster                                                       |
| deepcopy_memo           | 35.8 us                                                | 34.1 us: 1.05x faster                                                       |
| go                      | 140 ms                                                 | 133 ms: 1.05x faster                                                        |
| gunicorn                | 1.12 ms                                                | 1.06 ms: 1.05x faster                                                       |
| coroutines              | 26.2 ms                                                | 24.9 ms: 1.05x faster                                                       |
| docutils                | 2.60 sec                                               | 2.48 sec: 1.05x faster                                                      |
| unpack_sequence         | 44.5 ns                                                | 42.5 ns: 1.05x faster                                                       |
| deepcopy                | 341 us                                                 | 327 us: 1.04x faster                                                        |
| raytrace                | 291 ms                                                 | 280 ms: 1.04x faster                                                        |
| float                   | 76.8 ms                                                | 73.8 ms: 1.04x faster                                                       |
| spectral_norm           | 98.1 ms                                                | 94.4 ms: 1.04x faster                                                       |
| sqlglot_optimize        | 52.7 ms                                                | 50.7 ms: 1.04x faster                                                       |
| pyflate                 | 419 ms                                                 | 406 ms: 1.03x faster                                                        |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                                        |
| create_gc_cycles        | 1.52 ms                                                | 1.47 ms: 1.03x faster                                                       |
| tornado_http            | 96.5 ms                                                | 93.8 ms: 1.03x faster                                                       |
| dulwich_log             | 64.0 ms                                                | 62.1 ms: 1.03x faster                                                       |
| scimark_monte_carlo     | 68.0 ms                                                | 66.1 ms: 1.03x faster                                                       |
| logging_format          | 6.48 us                                                | 6.31 us: 1.03x faster                                                       |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.02x faster                                                        |
| crypto_pyaes            | 75.7 ms                                                | 74.0 ms: 1.02x faster                                                       |
| deepcopy_reduce         | 3.02 us                                                | 2.95 us: 1.02x faster                                                       |
| pidigits                | 197 ms                                                 | 193 ms: 1.02x faster                                                        |
| regex_effbot            | 3.46 ms                                                | 3.38 ms: 1.02x faster                                                       |
| mdp                     | 2.63 sec                                               | 2.57 sec: 1.02x faster                                                      |
| thrift                  | 760 us                                                 | 745 us: 1.02x faster                                                        |
| unpickle                | 13.3 us                                                | 13.0 us: 1.02x faster                                                       |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                        |
| async_generators        | 356 ms                                                 | 350 ms: 1.02x faster                                                        |
| scimark_lu              | 108 ms                                                 | 107 ms: 1.01x faster                                                        |
| coverage                | 99.3 ms                                                | 98.3 ms: 1.01x faster                                                       |
| unpickle_list           | 4.99 us                                                | 4.94 us: 1.01x faster                                                       |
| regex_dna               | 203 ms                                                 | 202 ms: 1.01x faster                                                        |
| xml_etree_process       | 53.7 ms                                                | 53.2 ms: 1.01x faster                                                       |
| telco                   | 6.43 ms                                                | 6.38 ms: 1.01x faster                                                       |
| pickle_dict             | 31.2 us                                                | 31.0 us: 1.01x faster                                                       |
| pathlib                 | 18.1 ms                                                | 18.0 ms: 1.01x faster                                                       |
| mako                    | 9.83 ms                                                | 9.85 ms: 1.00x slower                                                       |
| xml_etree_generate      | 75.9 ms                                                | 77.1 ms: 1.02x slower                                                       |
| pickle_list             | 4.14 us                                                | 4.22 us: 1.02x slower                                                       |
| sqlglot_transpile       | 1.65 ms                                                | 1.69 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed | 736 ms                                                 | 755 ms: 1.03x slower                                                        |
| sqlglot_parse           | 1.36 ms                                                | 1.40 ms: 1.03x slower                                                       |
| pickle                  | 9.90 us                                                | 10.2 us: 1.03x slower                                                       |
| python_startup          | 8.58 ms                                                | 8.93 ms: 1.04x slower                                                       |
| generators              | 73.5 ms                                                | 76.9 ms: 1.05x slower                                                       |
| sqlite_synth            | 2.48 us                                                | 2.62 us: 1.06x slower                                                       |
| nbody                   | 90.0 ms                                                | 95.6 ms: 1.06x slower                                                       |
| python_startup_no_site  | 6.04 ms                                                | 6.46 ms: 1.07x slower                                                       |
| gc_traversal            | 3.82 ms                                                | 4.29 ms: 1.12x slower                                                       |
| dask                    | 365 ms                                                 | 492 ms: 1.35x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                                |

Benchmark hidden because not significant (8): djangocms, async_tree_none, meteor_contest, chameleon, django_template, bench_mp_pool, async_tree_io, async_tree_memoization
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230129-3.12.0a4+-23ae36b/bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b.json: mypy
