
# Results vs. 3.11.0

- fork: brandtbucher
- ref: quicken_at_runtime
- machine: linux-x86_64
- commit hash: 57469f4
- commit date: 2023-01-28
- overall geometric mean: 1.02x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 254 ms: 1.01x faster                                                       |
| docutils       | 2.60 sec                                               | 2.51 sec: 1.03x faster                                                     |
| html5lib       | 63.2 ms                                                | 61.4 ms: 1.03x faster                                                      |
| tornado_http   | 96.6 ms                                                | 94.3 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                                               |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                 | 192 ms: 1.04x faster                                                       |
| nbody          | 95.0 ms                                                | 92.3 ms: 1.03x faster                                                      |
| float          | 76.3 ms                                                | 75.1 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 131 ms: 1.04x faster                                                       |
| regex_v8       | 22.3 ms                                                | 22.7 ms: 1.02x slower                                                      |
| regex_effbot   | 3.36 ms                                                | 3.60 ms: 1.07x slower                                                      |
| regex_dna      | 203 ms                                                 | 219 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                  | 1.03x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.40 ms: 1.35x faster                                                      |
| json_loads           | 26.2 us                                                | 23.9 us: 1.10x faster                                                      |
| unpickle_pure_python | 225 us                                                 | 208 us: 1.08x faster                                                       |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                       |
| pickle_pure_python   | 304 us                                                 | 292 us: 1.04x faster                                                       |
| pickle_list          | 4.17 us                                                | 4.06 us: 1.03x faster                                                      |
| pickle_dict          | 31.4 us                                                | 30.8 us: 1.02x faster                                                      |
| xml_etree_generate   | 76.2 ms                                                | 77.5 ms: 1.02x slower                                                      |
| pickle               | 9.79 us                                                | 9.98 us: 1.02x slower                                                      |
| unpickle_list        | 4.95 us                                                | 5.07 us: 1.02x slower                                                      |
| xml_etree_iterparse  | 103 ms                                                 | 106 ms: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                               |

Benchmark hidden because not significant (2): unpickle, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.70 ms: 1.04x slower                                                      |
| python_startup_no_site | 5.96 ms                                                | 6.23 ms: 1.04x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml     | 52.1 ms                                                | 46.4 ms: 1.12x faster                                                      |
| genshi_text    | 22.1 ms                                                | 20.6 ms: 1.07x faster                                                      |
| mako           | 9.85 ms                                                | 9.44 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                  | 1.06x faster                                                               |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.40 ms: 1.35x faster                                                      |
| genshi_xml              | 52.1 ms                                                | 46.4 ms: 1.12x faster                                                      |
| scimark_sparse_mat_mult | 4.40 ms                                                | 3.94 ms: 1.12x faster                                                      |
| json_loads              | 26.2 us                                                | 23.9 us: 1.10x faster                                                      |
| logging_silent          | 98.5 ns                                                | 90.2 ns: 1.09x faster                                                      |
| scimark_fft             | 329 ms                                                 | 302 ms: 1.09x faster                                                       |
| nqueens                 | 85.0 ms                                                | 78.0 ms: 1.09x faster                                                      |
| deltablue               | 3.64 ms                                                | 3.35 ms: 1.09x faster                                                      |
| unpickle_pure_python    | 225 us                                                 | 208 us: 1.08x faster                                                       |
| richards                | 46.2 ms                                                | 42.9 ms: 1.08x faster                                                      |
| genshi_text             | 22.1 ms                                                | 20.6 ms: 1.07x faster                                                      |
| json                    | 4.95 ms                                                | 4.61 ms: 1.07x faster                                                      |
| mdp                     | 2.62 sec                                               | 2.45 sec: 1.07x faster                                                     |
| deepcopy_memo           | 36.4 us                                                | 34.0 us: 1.07x faster                                                      |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                       |
| sympy_str               | 287 ms                                                 | 270 ms: 1.07x faster                                                       |
| sympy_sum               | 166 ms                                                 | 156 ms: 1.06x faster                                                       |
| deepcopy                | 344 us                                                 | 324 us: 1.06x faster                                                       |
| logging_simple          | 6.06 us                                                | 5.75 us: 1.05x faster                                                      |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.05x faster                                                      |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.05x faster                                                      |
| sympy_integrate         | 20.9 ms                                                | 20.0 ms: 1.05x faster                                                      |
| telco                   | 6.62 ms                                                | 6.34 ms: 1.04x faster                                                      |
| mako                    | 9.85 ms                                                | 9.44 ms: 1.04x faster                                                      |
| chaos                   | 68.6 ms                                                | 65.9 ms: 1.04x faster                                                      |
| unpack_sequence         | 43.4 ns                                                | 41.7 ns: 1.04x faster                                                      |
| spectral_norm           | 99.9 ms                                                | 96.1 ms: 1.04x faster                                                      |
| sqlglot_optimize        | 53.0 ms                                                | 51.0 ms: 1.04x faster                                                      |
| regex_compile           | 136 ms                                                 | 131 ms: 1.04x faster                                                       |
| sympy_expand            | 472 ms                                                 | 454 ms: 1.04x faster                                                       |
| logging_format          | 6.62 us                                                | 6.37 us: 1.04x faster                                                      |
| pickle_pure_python      | 304 us                                                 | 292 us: 1.04x faster                                                       |
| pidigits                | 199 ms                                                 | 192 ms: 1.04x faster                                                       |
| bench_thread_pool       | 810 us                                                 | 783 us: 1.03x faster                                                       |
| docutils                | 2.60 sec                                               | 2.51 sec: 1.03x faster                                                     |
| pathlib                 | 18.2 ms                                                | 17.6 ms: 1.03x faster                                                      |
| hexiom                  | 6.35 ms                                                | 6.16 ms: 1.03x faster                                                      |
| nbody                   | 95.0 ms                                                | 92.3 ms: 1.03x faster                                                      |
| raytrace                | 290 ms                                                 | 282 ms: 1.03x faster                                                       |
| html5lib                | 63.2 ms                                                | 61.4 ms: 1.03x faster                                                      |
| pickle_list             | 4.17 us                                                | 4.06 us: 1.03x faster                                                      |
| pprint_pformat          | 1.44 sec                                               | 1.41 sec: 1.03x faster                                                     |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                       |
| tornado_http            | 96.6 ms                                                | 94.3 ms: 1.02x faster                                                      |
| go                      | 143 ms                                                 | 140 ms: 1.02x faster                                                       |
| pickle_dict             | 31.4 us                                                | 30.8 us: 1.02x faster                                                      |
| scimark_lu              | 107 ms                                                 | 105 ms: 1.02x faster                                                       |
| deepcopy_reduce         | 2.97 us                                                | 2.91 us: 1.02x faster                                                      |
| crypto_pyaes            | 73.9 ms                                                | 72.6 ms: 1.02x faster                                                      |
| float                   | 76.3 ms                                                | 75.1 ms: 1.02x faster                                                      |
| dulwich_log             | 63.9 ms                                                | 62.9 ms: 1.02x faster                                                      |
| async_tree_none         | 529 ms                                                 | 522 ms: 1.01x faster                                                       |
| scimark_monte_carlo     | 68.3 ms                                                | 67.3 ms: 1.01x faster                                                      |
| pprint_safe_repr        | 691 ms                                                 | 681 ms: 1.01x faster                                                       |
| pycparser               | 1.17 sec                                               | 1.16 sec: 1.01x faster                                                     |
| 2to3                    | 257 ms                                                 | 254 ms: 1.01x faster                                                       |
| async_generators        | 359 ms                                                 | 355 ms: 1.01x faster                                                       |
| thrift                  | 752 us                                                 | 744 us: 1.01x faster                                                       |
| coroutines              | 26.1 ms                                                | 26.0 ms: 1.00x faster                                                      |
| coverage                | 101 ms                                                 | 102 ms: 1.01x slower                                                       |
| regex_v8                | 22.3 ms                                                | 22.7 ms: 1.02x slower                                                      |
| xml_etree_generate      | 76.2 ms                                                | 77.5 ms: 1.02x slower                                                      |
| pickle                  | 9.79 us                                                | 9.98 us: 1.02x slower                                                      |
| unpickle_list           | 4.95 us                                                | 5.07 us: 1.02x slower                                                      |
| scimark_sor             | 115 ms                                                 | 118 ms: 1.03x slower                                                       |
| generators              | 72.2 ms                                                | 74.4 ms: 1.03x slower                                                      |
| xml_etree_iterparse     | 103 ms                                                 | 106 ms: 1.03x slower                                                       |
| pyflate                 | 417 ms                                                 | 432 ms: 1.04x slower                                                       |
| sqlglot_transpile       | 1.66 ms                                                | 1.72 ms: 1.04x slower                                                      |
| sqlite_synth            | 2.49 us                                                | 2.59 us: 1.04x slower                                                      |
| python_startup          | 8.36 ms                                                | 8.70 ms: 1.04x slower                                                      |
| sqlglot_parse           | 1.37 ms                                                | 1.43 ms: 1.04x slower                                                      |
| python_startup_no_site  | 5.96 ms                                                | 6.23 ms: 1.04x slower                                                      |
| async_tree_memoization  | 625 ms                                                 | 661 ms: 1.06x slower                                                       |
| regex_effbot            | 3.36 ms                                                | 3.60 ms: 1.07x slower                                                      |
| regex_dna               | 203 ms                                                 | 219 ms: 1.08x slower                                                       |
| mypy                    | 669 ms                                                 | 807 ms: 1.21x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.02x faster                                                               |

Benchmark hidden because not significant (9): unpickle, fannkuch, async_tree_io, xml_etree_process, django_template, bench_mp_pool, chameleon, meteor_contest, async_tree_cpu_io_mixed
Ignored benchmarks (4) of /home/mdboom/Work/builds/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230128-3.12.0a4+-57469f4/bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
