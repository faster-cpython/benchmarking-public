
# Results vs. 3.11.0

- fork: brandtbucher
- ref: compare_and_not_bran
- machine: linux-x86_64
- commit hash: 49083fa
- commit date: 2023-02-01
- overall geometric mean: 1.02x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 253 ms: 1.02x faster                                                         |
| chameleon      | 6.41 ms                                                | 6.50 ms: 1.01x slower                                                        |
| docutils       | 2.60 sec                                               | 2.53 sec: 1.03x faster                                                       |
| html5lib       | 63.2 ms                                                | 61.0 ms: 1.04x faster                                                        |
| tornado_http   | 96.6 ms                                                | 94.6 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 73.8 ms: 1.03x faster                                                        |
| nbody          | 95.0 ms                                                | 93.3 ms: 1.02x faster                                                        |
| pidigits       | 199 ms                                                 | 198 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 134 ms: 1.02x faster                                                         |
| regex_v8       | 22.3 ms                                                | 22.6 ms: 1.01x slower                                                        |
| regex_dna      | 203 ms                                                 | 209 ms: 1.03x slower                                                         |
| regex_effbot   | 3.36 ms                                                | 3.54 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.41 ms: 1.35x faster                                                        |
| unpickle_pure_python | 225 us                                                 | 203 us: 1.11x faster                                                         |
| json_loads           | 26.2 us                                                | 24.3 us: 1.08x faster                                                        |
| pickle_pure_python   | 304 us                                                 | 290 us: 1.05x faster                                                         |
| xml_etree_parse      | 158 ms                                                 | 151 ms: 1.05x faster                                                         |
| xml_etree_process    | 53.8 ms                                                | 53.5 ms: 1.01x faster                                                        |
| xml_etree_generate   | 76.2 ms                                                | 77.5 ms: 1.02x slower                                                        |
| pickle_list          | 4.17 us                                                | 4.26 us: 1.02x slower                                                        |
| pickle_dict          | 31.4 us                                                | 32.1 us: 1.02x slower                                                        |
| xml_etree_iterparse  | 103 ms                                                 | 106 ms: 1.04x slower                                                         |
| pickle               | 9.79 us                                                | 10.3 us: 1.05x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (2): unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.94 ms: 1.07x slower                                                        |
| python_startup_no_site | 5.96 ms                                                | 6.46 ms: 1.08x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                | 47.5 ms: 1.10x faster                                                        |
| genshi_text     | 22.1 ms                                                | 20.7 ms: 1.07x faster                                                        |
| mako            | 9.85 ms                                                | 9.78 ms: 1.01x faster                                                        |
| django_template | 32.5 ms                                                | 33.4 ms: 1.03x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.41 ms: 1.35x faster                                                        |
| deltablue               | 3.64 ms                                                | 3.28 ms: 1.11x faster                                                        |
| nqueens                 | 85.0 ms                                                | 76.6 ms: 1.11x faster                                                        |
| unpickle_pure_python    | 225 us                                                 | 203 us: 1.11x faster                                                         |
| genshi_xml              | 52.1 ms                                                | 47.5 ms: 1.10x faster                                                        |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.07 ms: 1.08x faster                                                        |
| scimark_fft             | 329 ms                                                 | 305 ms: 1.08x faster                                                         |
| json_loads              | 26.2 us                                                | 24.3 us: 1.08x faster                                                        |
| hexiom                  | 6.35 ms                                                | 5.89 ms: 1.08x faster                                                        |
| richards                | 46.2 ms                                                | 43.0 ms: 1.07x faster                                                        |
| genshi_text             | 22.1 ms                                                | 20.7 ms: 1.07x faster                                                        |
| sympy_sum               | 166 ms                                                 | 155 ms: 1.07x faster                                                         |
| sympy_str               | 287 ms                                                 | 269 ms: 1.07x faster                                                         |
| fannkuch                | 388 ms                                                 | 364 ms: 1.07x faster                                                         |
| json                    | 4.95 ms                                                | 4.69 ms: 1.05x faster                                                        |
| sympy_integrate         | 20.9 ms                                                | 19.8 ms: 1.05x faster                                                        |
| scimark_sor             | 115 ms                                                 | 109 ms: 1.05x faster                                                         |
| spectral_norm           | 99.9 ms                                                | 95.2 ms: 1.05x faster                                                        |
| aiohttp                 | 1.05 ms                                                | 997 us: 1.05x faster                                                         |
| logging_simple          | 6.06 us                                                | 5.80 us: 1.05x faster                                                        |
| pickle_pure_python      | 304 us                                                 | 290 us: 1.05x faster                                                         |
| xml_etree_parse         | 158 ms                                                 | 151 ms: 1.05x faster                                                         |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.05x faster                                                        |
| deepcopy_memo           | 36.4 us                                                | 34.9 us: 1.04x faster                                                        |
| sqlglot_optimize        | 53.0 ms                                                | 50.8 ms: 1.04x faster                                                        |
| sympy_expand            | 472 ms                                                 | 454 ms: 1.04x faster                                                         |
| bench_thread_pool       | 810 us                                                 | 779 us: 1.04x faster                                                         |
| chaos                   | 68.6 ms                                                | 66.1 ms: 1.04x faster                                                        |
| html5lib                | 63.2 ms                                                | 61.0 ms: 1.04x faster                                                        |
| float                   | 76.3 ms                                                | 73.8 ms: 1.03x faster                                                        |
| logging_format          | 6.62 us                                                | 6.40 us: 1.03x faster                                                        |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.03x faster                                                         |
| go                      | 143 ms                                                 | 139 ms: 1.03x faster                                                         |
| unpack_sequence         | 43.4 ns                                                | 42.0 ns: 1.03x faster                                                        |
| deepcopy                | 344 us                                                 | 333 us: 1.03x faster                                                         |
| logging_silent          | 98.5 ns                                                | 95.5 ns: 1.03x faster                                                        |
| raytrace                | 290 ms                                                 | 281 ms: 1.03x faster                                                         |
| coroutines              | 26.1 ms                                                | 25.3 ms: 1.03x faster                                                        |
| docutils                | 2.60 sec                                               | 2.53 sec: 1.03x faster                                                       |
| pyflate                 | 417 ms                                                 | 407 ms: 1.03x faster                                                         |
| pprint_pformat          | 1.44 sec                                               | 1.41 sec: 1.02x faster                                                       |
| dulwich_log             | 63.9 ms                                                | 62.4 ms: 1.02x faster                                                        |
| async_generators        | 359 ms                                                 | 351 ms: 1.02x faster                                                         |
| coverage                | 101 ms                                                 | 98.3 ms: 1.02x faster                                                        |
| tornado_http            | 96.6 ms                                                | 94.6 ms: 1.02x faster                                                        |
| scimark_lu              | 107 ms                                                 | 105 ms: 1.02x faster                                                         |
| scimark_monte_carlo     | 68.3 ms                                                | 67.0 ms: 1.02x faster                                                        |
| 2to3                    | 257 ms                                                 | 253 ms: 1.02x faster                                                         |
| nbody                   | 95.0 ms                                                | 93.3 ms: 1.02x faster                                                        |
| deepcopy_reduce         | 2.97 us                                                | 2.91 us: 1.02x faster                                                        |
| regex_compile           | 136 ms                                                 | 134 ms: 1.02x faster                                                         |
| telco                   | 6.62 ms                                                | 6.52 ms: 1.02x faster                                                        |
| crypto_pyaes            | 73.9 ms                                                | 72.8 ms: 1.01x faster                                                        |
| pprint_safe_repr        | 691 ms                                                 | 681 ms: 1.01x faster                                                         |
| pycparser               | 1.17 sec                                               | 1.16 sec: 1.01x faster                                                       |
| meteor_contest          | 105 ms                                                 | 104 ms: 1.01x faster                                                         |
| pidigits                | 199 ms                                                 | 198 ms: 1.01x faster                                                         |
| mako                    | 9.85 ms                                                | 9.78 ms: 1.01x faster                                                        |
| pathlib                 | 18.2 ms                                                | 18.0 ms: 1.01x faster                                                        |
| xml_etree_process       | 53.8 ms                                                | 53.5 ms: 1.01x faster                                                        |
| thrift                  | 752 us                                                 | 756 us: 1.01x slower                                                         |
| regex_v8                | 22.3 ms                                                | 22.6 ms: 1.01x slower                                                        |
| chameleon               | 6.41 ms                                                | 6.50 ms: 1.01x slower                                                        |
| xml_etree_generate      | 76.2 ms                                                | 77.5 ms: 1.02x slower                                                        |
| mdp                     | 2.62 sec                                               | 2.68 sec: 1.02x slower                                                       |
| pickle_list             | 4.17 us                                                | 4.26 us: 1.02x slower                                                        |
| pickle_dict             | 31.4 us                                                | 32.1 us: 1.02x slower                                                        |
| async_tree_memoization  | 625 ms                                                 | 642 ms: 1.03x slower                                                         |
| django_template         | 32.5 ms                                                | 33.4 ms: 1.03x slower                                                        |
| regex_dna               | 203 ms                                                 | 209 ms: 1.03x slower                                                         |
| xml_etree_iterparse     | 103 ms                                                 | 106 ms: 1.04x slower                                                         |
| sqlite_synth            | 2.49 us                                                | 2.58 us: 1.04x slower                                                        |
| sqlglot_transpile       | 1.66 ms                                                | 1.73 ms: 1.04x slower                                                        |
| generators              | 72.2 ms                                                | 75.4 ms: 1.05x slower                                                        |
| pickle                  | 9.79 us                                                | 10.3 us: 1.05x slower                                                        |
| sqlglot_parse           | 1.37 ms                                                | 1.44 ms: 1.05x slower                                                        |
| regex_effbot            | 3.36 ms                                                | 3.54 ms: 1.05x slower                                                        |
| python_startup          | 8.36 ms                                                | 8.94 ms: 1.07x slower                                                        |
| python_startup_no_site  | 5.96 ms                                                | 6.46 ms: 1.08x slower                                                        |
| mypy                    | 669 ms                                                 | 807 ms: 1.21x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.02x faster                                                                 |

Benchmark hidden because not significant (6): async_tree_none, async_tree_cpu_io_mixed, async_tree_io, bench_mp_pool, unpickle_list, unpickle
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230201-3.12.0a4+-49083fa/bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
