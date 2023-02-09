
# Results vs. 3.11.0

- fork: brandtbucher
- ref: compare_and_not_bran
- machine: linux-x86_64
- commit hash: 49083fa
- commit date: 2023-02-01
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 253 ms: 1.02x faster                                                         |
| chameleon      | 6.41 ms                                                | 6.47 ms: 1.01x slower                                                        |
| docutils       | 2.60 sec                                               | 2.53 sec: 1.03x faster                                                       |
| html5lib       | 63.2 ms                                                | 61.4 ms: 1.03x faster                                                        |
| tornado_http   | 96.6 ms                                                | 94.9 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 72.7 ms: 1.05x faster                                                        |
| pidigits       | 199 ms                                                 | 198 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.06x faster                                                         |
| regex_v8       | 22.3 ms                                                | 22.5 ms: 1.01x slower                                                        |
| regex_dna      | 203 ms                                                 | 217 ms: 1.07x slower                                                         |
| regex_effbot   | 3.36 ms                                                | 3.63 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.33 ms: 1.36x faster                                                        |
| unpickle_pure_python | 225 us                                                 | 202 us: 1.12x faster                                                         |
| json_loads           | 26.2 us                                                | 23.9 us: 1.10x faster                                                        |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.08x faster                                                         |
| pickle_pure_python   | 304 us                                                 | 287 us: 1.06x faster                                                         |
| unpickle             | 13.3 us                                                | 13.0 us: 1.02x faster                                                        |
| xml_etree_process    | 53.8 ms                                                | 54.0 ms: 1.01x slower                                                        |
| unpickle_list        | 4.95 us                                                | 5.02 us: 1.01x slower                                                        |
| xml_etree_generate   | 76.2 ms                                                | 78.0 ms: 1.02x slower                                                        |
| pickle_dict          | 31.4 us                                                | 32.2 us: 1.02x slower                                                        |
| pickle_list          | 4.17 us                                                | 4.31 us: 1.03x slower                                                        |
| pickle               | 9.79 us                                                | 10.2 us: 1.04x slower                                                        |
| xml_etree_iterparse  | 103 ms                                                 | 107 ms: 1.04x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.88 ms: 1.06x slower                                                        |
| python_startup_no_site | 5.96 ms                                                | 6.43 ms: 1.08x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml     | 52.1 ms                                                | 46.3 ms: 1.12x faster                                                        |
| genshi_text    | 22.1 ms                                                | 20.6 ms: 1.07x faster                                                        |
| mako           | 9.85 ms                                                | 9.75 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.33 ms: 1.36x faster                                                        |
| genshi_xml              | 52.1 ms                                                | 46.3 ms: 1.12x faster                                                        |
| deltablue               | 3.64 ms                                                | 3.25 ms: 1.12x faster                                                        |
| unpickle_pure_python    | 225 us                                                 | 202 us: 1.12x faster                                                         |
| richards                | 46.2 ms                                                | 41.5 ms: 1.11x faster                                                        |
| nqueens                 | 85.0 ms                                                | 76.6 ms: 1.11x faster                                                        |
| scimark_sparse_mat_mult | 4.40 ms                                                | 3.98 ms: 1.11x faster                                                        |
| json_loads              | 26.2 us                                                | 23.9 us: 1.10x faster                                                        |
| scimark_fft             | 329 ms                                                 | 302 ms: 1.09x faster                                                         |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.08x faster                                                         |
| hexiom                  | 6.35 ms                                                | 5.92 ms: 1.07x faster                                                        |
| deepcopy                | 344 us                                                 | 321 us: 1.07x faster                                                         |
| genshi_text             | 22.1 ms                                                | 20.6 ms: 1.07x faster                                                        |
| spectral_norm           | 99.9 ms                                                | 93.4 ms: 1.07x faster                                                        |
| deepcopy_memo           | 36.4 us                                                | 34.2 us: 1.07x faster                                                        |
| json                    | 4.95 ms                                                | 4.64 ms: 1.07x faster                                                        |
| sympy_str               | 287 ms                                                 | 270 ms: 1.06x faster                                                         |
| sympy_sum               | 166 ms                                                 | 156 ms: 1.06x faster                                                         |
| logging_silent          | 98.5 ns                                                | 92.7 ns: 1.06x faster                                                        |
| chaos                   | 68.6 ms                                                | 64.7 ms: 1.06x faster                                                        |
| pickle_pure_python      | 304 us                                                 | 287 us: 1.06x faster                                                         |
| regex_compile           | 136 ms                                                 | 128 ms: 1.06x faster                                                         |
| fannkuch                | 388 ms                                                 | 367 ms: 1.06x faster                                                         |
| scimark_sor             | 115 ms                                                 | 109 ms: 1.06x faster                                                         |
| sympy_integrate         | 20.9 ms                                                | 19.8 ms: 1.05x faster                                                        |
| logging_simple          | 6.06 us                                                | 5.77 us: 1.05x faster                                                        |
| aiohttp                 | 1.05 ms                                                | 996 us: 1.05x faster                                                         |
| float                   | 76.3 ms                                                | 72.7 ms: 1.05x faster                                                        |
| go                      | 143 ms                                                 | 137 ms: 1.05x faster                                                         |
| pprint_pformat          | 1.44 sec                                               | 1.38 sec: 1.04x faster                                                       |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.04x faster                                                        |
| sqlglot_optimize        | 53.0 ms                                                | 50.9 ms: 1.04x faster                                                        |
| sympy_expand            | 472 ms                                                 | 454 ms: 1.04x faster                                                         |
| pyflate                 | 417 ms                                                 | 402 ms: 1.04x faster                                                         |
| logging_format          | 6.62 us                                                | 6.38 us: 1.04x faster                                                        |
| raytrace                | 290 ms                                                 | 280 ms: 1.04x faster                                                         |
| mdp                     | 2.62 sec                                               | 2.53 sec: 1.04x faster                                                       |
| bench_thread_pool       | 810 us                                                 | 781 us: 1.04x faster                                                         |
| pathlib                 | 18.2 ms                                                | 17.6 ms: 1.03x faster                                                        |
| scimark_monte_carlo     | 68.3 ms                                                | 66.1 ms: 1.03x faster                                                        |
| deepcopy_reduce         | 2.97 us                                                | 2.88 us: 1.03x faster                                                        |
| telco                   | 6.62 ms                                                | 6.44 ms: 1.03x faster                                                        |
| html5lib                | 63.2 ms                                                | 61.4 ms: 1.03x faster                                                        |
| docutils                | 2.60 sec                                               | 2.53 sec: 1.03x faster                                                       |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                         |
| scimark_lu              | 107 ms                                                 | 105 ms: 1.03x faster                                                         |
| pprint_safe_repr        | 691 ms                                                 | 674 ms: 1.02x faster                                                         |
| pycparser               | 1.17 sec                                               | 1.15 sec: 1.02x faster                                                       |
| unpickle                | 13.3 us                                                | 13.0 us: 1.02x faster                                                        |
| tornado_http            | 96.6 ms                                                | 94.9 ms: 1.02x faster                                                        |
| 2to3                    | 257 ms                                                 | 253 ms: 1.02x faster                                                         |
| dulwich_log             | 63.9 ms                                                | 62.8 ms: 1.02x faster                                                        |
| async_generators        | 359 ms                                                 | 353 ms: 1.02x faster                                                         |
| mako                    | 9.85 ms                                                | 9.75 ms: 1.01x faster                                                        |
| unpack_sequence         | 43.4 ns                                                | 43.0 ns: 1.01x faster                                                        |
| pidigits                | 199 ms                                                 | 198 ms: 1.01x faster                                                         |
| xml_etree_process       | 53.8 ms                                                | 54.0 ms: 1.01x slower                                                        |
| regex_v8                | 22.3 ms                                                | 22.5 ms: 1.01x slower                                                        |
| thrift                  | 752 us                                                 | 758 us: 1.01x slower                                                         |
| chameleon               | 6.41 ms                                                | 6.47 ms: 1.01x slower                                                        |
| meteor_contest          | 105 ms                                                 | 106 ms: 1.01x slower                                                         |
| coroutines              | 26.1 ms                                                | 26.4 ms: 1.01x slower                                                        |
| unpickle_list           | 4.95 us                                                | 5.02 us: 1.01x slower                                                        |
| async_tree_io           | 1.31 sec                                               | 1.33 sec: 1.02x slower                                                       |
| xml_etree_generate      | 76.2 ms                                                | 78.0 ms: 1.02x slower                                                        |
| pickle_dict             | 31.4 us                                                | 32.2 us: 1.02x slower                                                        |
| async_tree_memoization  | 625 ms                                                 | 641 ms: 1.03x slower                                                         |
| pickle_list             | 4.17 us                                                | 4.31 us: 1.03x slower                                                        |
| sqlglot_transpile       | 1.66 ms                                                | 1.71 ms: 1.03x slower                                                        |
| sqlite_synth            | 2.49 us                                                | 2.59 us: 1.04x slower                                                        |
| pickle                  | 9.79 us                                                | 10.2 us: 1.04x slower                                                        |
| xml_etree_iterparse     | 103 ms                                                 | 107 ms: 1.04x slower                                                         |
| sqlglot_parse           | 1.37 ms                                                | 1.43 ms: 1.04x slower                                                        |
| python_startup          | 8.36 ms                                                | 8.88 ms: 1.06x slower                                                        |
| regex_dna               | 203 ms                                                 | 217 ms: 1.07x slower                                                         |
| generators              | 72.2 ms                                                | 77.3 ms: 1.07x slower                                                        |
| python_startup_no_site  | 5.96 ms                                                | 6.43 ms: 1.08x slower                                                        |
| regex_effbot            | 3.36 ms                                                | 3.63 ms: 1.08x slower                                                        |
| mypy                    | 669 ms                                                 | 809 ms: 1.21x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (7): nbody, async_tree_none, crypto_pyaes, coverage, bench_mp_pool, async_tree_cpu_io_mixed, django_template
Ignored benchmarks (4) of /home/mdboom/Work/builds/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230201-3.12.0a4+-49083fa/bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
