
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
| 2to3           | 259 ms                                                 | 253 ms: 1.03x faster                                                         |
| chameleon      | 6.38 ms                                                | 6.47 ms: 1.01x slower                                                        |
| docutils       | 2.60 sec                                               | 2.53 sec: 1.03x faster                                                       |
| html5lib       | 64.8 ms                                                | 61.4 ms: 1.06x faster                                                        |
| tornado_http   | 96.5 ms                                                | 94.9 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.7 ms: 1.06x faster                                                        |
| pidigits       | 197 ms                                                 | 198 ms: 1.00x slower                                                         |
| nbody          | 90.0 ms                                                | 94.4 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.06x faster                                                         |
| regex_v8       | 22.2 ms                                                | 22.5 ms: 1.01x slower                                                        |
| regex_effbot   | 3.46 ms                                                | 3.63 ms: 1.05x slower                                                        |
| regex_dna      | 203 ms                                                 | 217 ms: 1.07x slower                                                         |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.33 ms: 1.32x faster                                                        |
| unpickle_pure_python | 227 us                                                 | 202 us: 1.12x faster                                                         |
| json_loads           | 26.1 us                                                | 23.9 us: 1.09x faster                                                        |
| xml_etree_parse      | 160 ms                                                 | 147 ms: 1.09x faster                                                         |
| pickle_pure_python   | 308 us                                                 | 287 us: 1.07x faster                                                         |
| unpickle             | 13.3 us                                                | 13.0 us: 1.02x faster                                                        |
| xml_etree_process    | 53.7 ms                                                | 54.0 ms: 1.01x slower                                                        |
| xml_etree_generate   | 75.9 ms                                                | 78.0 ms: 1.03x slower                                                        |
| xml_etree_iterparse  | 104 ms                                                 | 107 ms: 1.03x slower                                                         |
| pickle               | 9.90 us                                                | 10.2 us: 1.03x slower                                                        |
| pickle_dict          | 31.2 us                                                | 32.2 us: 1.03x slower                                                        |
| pickle_list          | 4.14 us                                                | 4.31 us: 1.04x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.88 ms: 1.04x slower                                                        |
| python_startup_no_site | 6.04 ms                                                | 6.43 ms: 1.06x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 46.3 ms: 1.11x faster                                                        |
| genshi_text     | 21.5 ms                                                | 20.6 ms: 1.04x faster                                                        |
| mako            | 9.83 ms                                                | 9.75 ms: 1.01x faster                                                        |
| django_template | 32.3 ms                                                | 32.6 ms: 1.01x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 494 ms: 1.79x faster                                                         |
| json_dumps              | 12.4 ms                                                | 9.33 ms: 1.32x faster                                                        |
| scimark_sparse_mat_mult | 4.59 ms                                                | 3.98 ms: 1.15x faster                                                        |
| deltablue               | 3.66 ms                                                | 3.25 ms: 1.13x faster                                                        |
| unpickle_pure_python    | 227 us                                                 | 202 us: 1.12x faster                                                         |
| genshi_xml              | 51.4 ms                                                | 46.3 ms: 1.11x faster                                                        |
| richards                | 46.1 ms                                                | 41.5 ms: 1.11x faster                                                        |
| nqueens                 | 83.8 ms                                                | 76.6 ms: 1.09x faster                                                        |
| json_loads              | 26.1 us                                                | 23.9 us: 1.09x faster                                                        |
| xml_etree_parse         | 160 ms                                                 | 147 ms: 1.09x faster                                                         |
| sympy_str               | 291 ms                                                 | 270 ms: 1.08x faster                                                         |
| scimark_fft             | 325 ms                                                 | 302 ms: 1.08x faster                                                         |
| pickle_pure_python      | 308 us                                                 | 287 us: 1.07x faster                                                         |
| hexiom                  | 6.34 ms                                                | 5.92 ms: 1.07x faster                                                        |
| deepcopy                | 341 us                                                 | 321 us: 1.07x faster                                                         |
| sympy_sum               | 166 ms                                                 | 156 ms: 1.06x faster                                                         |
| chaos                   | 68.7 ms                                                | 64.7 ms: 1.06x faster                                                        |
| regex_compile           | 136 ms                                                 | 128 ms: 1.06x faster                                                         |
| logging_silent          | 98.0 ns                                                | 92.7 ns: 1.06x faster                                                        |
| sympy_integrate         | 21.0 ms                                                | 19.8 ms: 1.06x faster                                                        |
| html5lib                | 64.8 ms                                                | 61.4 ms: 1.06x faster                                                        |
| float                   | 76.8 ms                                                | 72.7 ms: 1.06x faster                                                        |
| scimark_sor             | 115 ms                                                 | 109 ms: 1.06x faster                                                         |
| aiohttp                 | 1.05 ms                                                | 996 us: 1.05x faster                                                         |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.05x faster                                                       |
| spectral_norm           | 98.1 ms                                                | 93.4 ms: 1.05x faster                                                        |
| deepcopy_reduce         | 3.02 us                                                | 2.88 us: 1.05x faster                                                        |
| json                    | 4.87 ms                                                | 4.64 ms: 1.05x faster                                                        |
| fannkuch                | 384 ms                                                 | 367 ms: 1.05x faster                                                         |
| deepcopy_memo           | 35.8 us                                                | 34.2 us: 1.05x faster                                                        |
| sympy_expand            | 475 ms                                                 | 454 ms: 1.05x faster                                                         |
| pprint_safe_repr        | 706 ms                                                 | 674 ms: 1.05x faster                                                         |
| bench_thread_pool       | 817 us                                                 | 781 us: 1.05x faster                                                         |
| genshi_text             | 21.5 ms                                                | 20.6 ms: 1.04x faster                                                        |
| logging_simple          | 6.02 us                                                | 5.77 us: 1.04x faster                                                        |
| pyflate                 | 419 ms                                                 | 402 ms: 1.04x faster                                                         |
| raytrace                | 291 ms                                                 | 280 ms: 1.04x faster                                                         |
| mdp                     | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                       |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.04x faster                                                        |
| create_gc_cycles        | 1.52 ms                                                | 1.46 ms: 1.04x faster                                                        |
| sqlglot_optimize        | 52.7 ms                                                | 50.9 ms: 1.04x faster                                                        |
| unpack_sequence         | 44.5 ns                                                | 43.0 ns: 1.03x faster                                                        |
| pycparser               | 1.19 sec                                               | 1.15 sec: 1.03x faster                                                       |
| scimark_lu              | 108 ms                                                 | 105 ms: 1.03x faster                                                         |
| docutils                | 2.60 sec                                               | 2.53 sec: 1.03x faster                                                       |
| scimark_monte_carlo     | 68.0 ms                                                | 66.1 ms: 1.03x faster                                                        |
| pathlib                 | 18.1 ms                                                | 17.6 ms: 1.03x faster                                                        |
| crypto_pyaes            | 75.7 ms                                                | 73.7 ms: 1.03x faster                                                        |
| 2to3                    | 259 ms                                                 | 253 ms: 1.03x faster                                                         |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.02x faster                                                         |
| go                      | 140 ms                                                 | 137 ms: 1.02x faster                                                         |
| unpickle                | 13.3 us                                                | 13.0 us: 1.02x faster                                                        |
| dulwich_log             | 64.0 ms                                                | 62.8 ms: 1.02x faster                                                        |
| tornado_http            | 96.5 ms                                                | 94.9 ms: 1.02x faster                                                        |
| logging_format          | 6.48 us                                                | 6.38 us: 1.02x faster                                                        |
| mako                    | 9.83 ms                                                | 9.75 ms: 1.01x faster                                                        |
| async_generators        | 356 ms                                                 | 353 ms: 1.01x faster                                                         |
| pidigits                | 197 ms                                                 | 198 ms: 1.00x slower                                                         |
| xml_etree_process       | 53.7 ms                                                | 54.0 ms: 1.01x slower                                                        |
| django_template         | 32.3 ms                                                | 32.6 ms: 1.01x slower                                                        |
| coroutines              | 26.2 ms                                                | 26.4 ms: 1.01x slower                                                        |
| regex_v8                | 22.2 ms                                                | 22.5 ms: 1.01x slower                                                        |
| coverage                | 99.3 ms                                                | 100 ms: 1.01x slower                                                         |
| meteor_contest          | 104 ms                                                 | 106 ms: 1.01x slower                                                         |
| chameleon               | 6.38 ms                                                | 6.47 ms: 1.01x slower                                                        |
| async_tree_cpu_io_mixed | 736 ms                                                 | 753 ms: 1.02x slower                                                         |
| async_tree_io           | 1.30 sec                                               | 1.33 sec: 1.02x slower                                                       |
| async_tree_memoization  | 624 ms                                                 | 641 ms: 1.03x slower                                                         |
| xml_etree_generate      | 75.9 ms                                                | 78.0 ms: 1.03x slower                                                        |
| xml_etree_iterparse     | 104 ms                                                 | 107 ms: 1.03x slower                                                         |
| pickle                  | 9.90 us                                                | 10.2 us: 1.03x slower                                                        |
| pickle_dict             | 31.2 us                                                | 32.2 us: 1.03x slower                                                        |
| python_startup          | 8.58 ms                                                | 8.88 ms: 1.04x slower                                                        |
| sqlglot_transpile       | 1.65 ms                                                | 1.71 ms: 1.04x slower                                                        |
| pickle_list             | 4.14 us                                                | 4.31 us: 1.04x slower                                                        |
| sqlite_synth            | 2.48 us                                                | 2.59 us: 1.04x slower                                                        |
| nbody                   | 90.0 ms                                                | 94.4 ms: 1.05x slower                                                        |
| sqlglot_parse           | 1.36 ms                                                | 1.43 ms: 1.05x slower                                                        |
| regex_effbot            | 3.46 ms                                                | 3.63 ms: 1.05x slower                                                        |
| generators              | 73.5 ms                                                | 77.3 ms: 1.05x slower                                                        |
| python_startup_no_site  | 6.04 ms                                                | 6.43 ms: 1.06x slower                                                        |
| regex_dna               | 203 ms                                                 | 217 ms: 1.07x slower                                                         |
| gc_traversal            | 3.82 ms                                                | 4.27 ms: 1.12x slower                                                        |
| dask                    | 365 ms                                                 | 507 ms: 1.39x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (6): thrift, async_tree_none, bench_mp_pool, telco, djangocms, unpickle_list
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230201-3.12.0a4+-49083fa/bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa.json: mypy
