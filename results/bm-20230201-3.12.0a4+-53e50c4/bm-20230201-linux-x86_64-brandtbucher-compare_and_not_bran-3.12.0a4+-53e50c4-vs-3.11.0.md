
# Results vs. 3.11.0

- fork: brandtbucher
- ref: compare_and_not_bran
- machine: linux-x86_64
- commit hash: 53e50c4
- commit date: 2023-02-01
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 254 ms: 1.01x faster                                                         |
| chameleon      | 6.41 ms                                                | 6.44 ms: 1.01x slower                                                        |
| docutils       | 2.60 sec                                               | 2.55 sec: 1.02x faster                                                       |
| html5lib       | 63.2 ms                                                | 61.3 ms: 1.03x faster                                                        |
| tornado_http   | 96.6 ms                                                | 94.1 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 72.6 ms: 1.05x faster                                                        |
| pidigits       | 199 ms                                                 | 190 ms: 1.05x faster                                                         |
| nbody          | 95.0 ms                                                | 93.7 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 130 ms: 1.04x faster                                                         |
| regex_v8       | 22.3 ms                                                | 22.2 ms: 1.01x faster                                                        |
| regex_dna      | 203 ms                                                 | 210 ms: 1.03x slower                                                         |
| regex_effbot   | 3.36 ms                                                | 3.52 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.62 ms: 1.32x faster                                                        |
| unpickle_pure_python | 225 us                                                 | 202 us: 1.11x faster                                                         |
| json_loads           | 26.2 us                                                | 24.0 us: 1.09x faster                                                        |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.08x faster                                                         |
| pickle_pure_python   | 304 us                                                 | 288 us: 1.05x faster                                                         |
| pickle_dict          | 31.4 us                                                | 30.7 us: 1.02x faster                                                        |
| unpickle             | 13.3 us                                                | 13.0 us: 1.02x faster                                                        |
| pickle_list          | 4.17 us                                                | 4.10 us: 1.02x faster                                                        |
| xml_etree_process    | 53.8 ms                                                | 54.1 ms: 1.01x slower                                                        |
| xml_etree_generate   | 76.2 ms                                                | 77.7 ms: 1.02x slower                                                        |
| xml_etree_iterparse  | 103 ms                                                 | 105 ms: 1.02x slower                                                         |
| pickle               | 9.79 us                                                | 10.2 us: 1.04x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.89 ms: 1.06x slower                                                        |
| python_startup_no_site | 5.96 ms                                                | 6.44 ms: 1.08x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                | 46.6 ms: 1.12x faster                                                        |
| genshi_text     | 22.1 ms                                                | 20.4 ms: 1.08x faster                                                        |
| mako            | 9.85 ms                                                | 9.69 ms: 1.02x faster                                                        |
| django_template | 32.5 ms                                                | 32.3 ms: 1.01x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.62 ms: 1.32x faster                                                        |
| deltablue               | 3.64 ms                                                | 3.21 ms: 1.13x faster                                                        |
| genshi_xml              | 52.1 ms                                                | 46.6 ms: 1.12x faster                                                        |
| unpickle_pure_python    | 225 us                                                 | 202 us: 1.11x faster                                                         |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.00 ms: 1.10x faster                                                        |
| richards                | 46.2 ms                                                | 42.1 ms: 1.10x faster                                                        |
| json_loads              | 26.2 us                                                | 24.0 us: 1.09x faster                                                        |
| scimark_fft             | 329 ms                                                 | 302 ms: 1.09x faster                                                         |
| genshi_text             | 22.1 ms                                                | 20.4 ms: 1.08x faster                                                        |
| hexiom                  | 6.35 ms                                                | 5.89 ms: 1.08x faster                                                        |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.08x faster                                                         |
| nqueens                 | 85.0 ms                                                | 79.0 ms: 1.08x faster                                                        |
| sympy_sum               | 166 ms                                                 | 155 ms: 1.07x faster                                                         |
| fannkuch                | 388 ms                                                 | 364 ms: 1.07x faster                                                         |
| scimark_sor             | 115 ms                                                 | 108 ms: 1.06x faster                                                         |
| sympy_str               | 287 ms                                                 | 270 ms: 1.06x faster                                                         |
| sympy_integrate         | 20.9 ms                                                | 19.7 ms: 1.06x faster                                                        |
| spectral_norm           | 99.9 ms                                                | 94.5 ms: 1.06x faster                                                        |
| chaos                   | 68.6 ms                                                | 65.0 ms: 1.06x faster                                                        |
| pickle_pure_python      | 304 us                                                 | 288 us: 1.05x faster                                                         |
| float                   | 76.3 ms                                                | 72.6 ms: 1.05x faster                                                        |
| json                    | 4.95 ms                                                | 4.70 ms: 1.05x faster                                                        |
| deepcopy_memo           | 36.4 us                                                | 34.7 us: 1.05x faster                                                        |
| aiohttp                 | 1.05 ms                                                | 995 us: 1.05x faster                                                         |
| pidigits                | 199 ms                                                 | 190 ms: 1.05x faster                                                         |
| logging_silent          | 98.5 ns                                                | 93.7 ns: 1.05x faster                                                        |
| scimark_monte_carlo     | 68.3 ms                                                | 65.0 ms: 1.05x faster                                                        |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.05x faster                                                        |
| logging_simple          | 6.06 us                                                | 5.78 us: 1.05x faster                                                        |
| go                      | 143 ms                                                 | 137 ms: 1.05x faster                                                         |
| pprint_pformat          | 1.44 sec                                               | 1.38 sec: 1.05x faster                                                       |
| deepcopy                | 344 us                                                 | 329 us: 1.05x faster                                                         |
| coverage                | 101 ms                                                 | 96.1 ms: 1.05x faster                                                        |
| regex_compile           | 136 ms                                                 | 130 ms: 1.04x faster                                                         |
| pyflate                 | 417 ms                                                 | 400 ms: 1.04x faster                                                         |
| sympy_expand            | 472 ms                                                 | 454 ms: 1.04x faster                                                         |
| sqlglot_optimize        | 53.0 ms                                                | 51.0 ms: 1.04x faster                                                        |
| logging_format          | 6.62 us                                                | 6.38 us: 1.04x faster                                                        |
| telco                   | 6.62 ms                                                | 6.40 ms: 1.04x faster                                                        |
| raytrace                | 290 ms                                                 | 281 ms: 1.03x faster                                                         |
| html5lib                | 63.2 ms                                                | 61.3 ms: 1.03x faster                                                        |
| bench_thread_pool       | 810 us                                                 | 787 us: 1.03x faster                                                         |
| tornado_http            | 96.6 ms                                                | 94.1 ms: 1.03x faster                                                        |
| pprint_safe_repr        | 691 ms                                                 | 675 ms: 1.02x faster                                                         |
| pathlib                 | 18.2 ms                                                | 17.7 ms: 1.02x faster                                                        |
| scimark_lu              | 107 ms                                                 | 105 ms: 1.02x faster                                                         |
| pycparser               | 1.17 sec                                               | 1.15 sec: 1.02x faster                                                       |
| pickle_dict             | 31.4 us                                                | 30.7 us: 1.02x faster                                                        |
| unpickle                | 13.3 us                                                | 13.0 us: 1.02x faster                                                        |
| coroutines              | 26.1 ms                                                | 25.5 ms: 1.02x faster                                                        |
| docutils                | 2.60 sec                                               | 2.55 sec: 1.02x faster                                                       |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.02x faster                                                         |
| pickle_list             | 4.17 us                                                | 4.10 us: 1.02x faster                                                        |
| mdp                     | 2.62 sec                                               | 2.58 sec: 1.02x faster                                                       |
| dulwich_log             | 63.9 ms                                                | 62.8 ms: 1.02x faster                                                        |
| async_generators        | 359 ms                                                 | 353 ms: 1.02x faster                                                         |
| mako                    | 9.85 ms                                                | 9.69 ms: 1.02x faster                                                        |
| 2to3                    | 257 ms                                                 | 254 ms: 1.01x faster                                                         |
| nbody                   | 95.0 ms                                                | 93.7 ms: 1.01x faster                                                        |
| crypto_pyaes            | 73.9 ms                                                | 72.9 ms: 1.01x faster                                                        |
| deepcopy_reduce         | 2.97 us                                                | 2.93 us: 1.01x faster                                                        |
| thrift                  | 752 us                                                 | 744 us: 1.01x faster                                                         |
| django_template         | 32.5 ms                                                | 32.3 ms: 1.01x faster                                                        |
| regex_v8                | 22.3 ms                                                | 22.2 ms: 1.01x faster                                                        |
| chameleon               | 6.41 ms                                                | 6.44 ms: 1.01x slower                                                        |
| xml_etree_process       | 53.8 ms                                                | 54.1 ms: 1.01x slower                                                        |
| async_tree_cpu_io_mixed | 752 ms                                                 | 759 ms: 1.01x slower                                                         |
| async_tree_io           | 1.31 sec                                               | 1.33 sec: 1.02x slower                                                       |
| xml_etree_generate      | 76.2 ms                                                | 77.7 ms: 1.02x slower                                                        |
| xml_etree_iterparse     | 103 ms                                                 | 105 ms: 1.02x slower                                                         |
| sqlglot_transpile       | 1.66 ms                                                | 1.71 ms: 1.03x slower                                                        |
| sqlite_synth            | 2.49 us                                                | 2.57 us: 1.03x slower                                                        |
| regex_dna               | 203 ms                                                 | 210 ms: 1.03x slower                                                         |
| sqlglot_parse           | 1.37 ms                                                | 1.42 ms: 1.04x slower                                                        |
| pickle                  | 9.79 us                                                | 10.2 us: 1.04x slower                                                        |
| regex_effbot            | 3.36 ms                                                | 3.52 ms: 1.05x slower                                                        |
| generators              | 72.2 ms                                                | 76.5 ms: 1.06x slower                                                        |
| python_startup          | 8.36 ms                                                | 8.89 ms: 1.06x slower                                                        |
| async_tree_memoization  | 625 ms                                                 | 666 ms: 1.07x slower                                                         |
| python_startup_no_site  | 5.96 ms                                                | 6.44 ms: 1.08x slower                                                        |
| mypy                    | 669 ms                                                 | 807 ms: 1.21x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (5): meteor_contest, bench_mp_pool, unpickle_list, async_tree_none, unpack_sequence
Ignored benchmarks (4) of /home/mdboom/Work/builds/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230201-3.12.0a4+-53e50c4/bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
