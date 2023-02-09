
# Results vs. 3.10.4

- fork: brandtbucher
- ref: compare_and_not_bran
- machine: linux-x86_64
- commit hash: 49083fa
- commit date: 2023-02-01
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 253 ms: 1.31x faster                                                         |
| chameleon      | 8.86 ms                                                | 6.47 ms: 1.37x faster                                                        |
| docutils       | 3.18 sec                                               | 2.53 sec: 1.26x faster                                                       |
| html5lib       | 85.8 ms                                                | 61.4 ms: 1.40x faster                                                        |
| tornado_http   | 128 ms                                                 | 94.9 ms: 1.35x faster                                                        |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 108 ms                                                 | 72.7 ms: 1.48x faster                                                        |
| nbody          | 136 ms                                                 | 94.4 ms: 1.44x faster                                                        |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                                         |
| Geometric mean | (ref)                                                  | 1.27x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 128 ms: 1.35x faster                                                         |
| regex_v8       | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                        |
| regex_dna      | 214 ms                                                 | 217 ms: 1.01x slower                                                         |
| regex_effbot   | 3.21 ms                                                | 3.63 ms: 1.13x slower                                                        |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 287 us: 1.58x faster                                                         |
| unpickle_pure_python | 297 us                                                 | 202 us: 1.47x faster                                                         |
| json_dumps           | 13.5 ms                                                | 9.33 ms: 1.44x faster                                                        |
| xml_etree_process    | 74.5 ms                                                | 54.0 ms: 1.38x faster                                                        |
| json_loads           | 28.9 us                                                | 23.9 us: 1.21x faster                                                        |
| xml_etree_generate   | 93.3 ms                                                | 78.0 ms: 1.20x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                         |
| unpickle             | 14.3 us                                                | 13.0 us: 1.10x faster                                                        |
| pickle_list          | 4.50 us                                                | 4.31 us: 1.04x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                 | 107 ms: 1.03x faster                                                         |
| pickle               | 10.1 us                                                | 10.2 us: 1.01x slower                                                        |
| pickle_dict          | 28.3 us                                                | 32.2 us: 1.14x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                                 |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.88 ms: 1.57x faster                                                        |
| python_startup_no_site | 5.76 ms                                                | 6.43 ms: 1.12x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.6 ms: 1.48x faster                                                        |
| mako            | 14.3 ms                                                | 9.75 ms: 1.46x faster                                                        |
| django_template | 46.3 ms                                                | 32.6 ms: 1.42x faster                                                        |
| genshi_xml      | 63.6 ms                                                | 46.3 ms: 1.37x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.25 ms: 2.28x faster                                                        |
| logging_silent          | 173 ns                                                 | 92.7 ns: 1.87x faster                                                        |
| scimark_sor             | 193 ms                                                 | 109 ms: 1.77x faster                                                         |
| richards                | 71.4 ms                                                | 41.5 ms: 1.72x faster                                                        |
| pyflate                 | 675 ms                                                 | 402 ms: 1.68x faster                                                         |
| go                      | 226 ms                                                 | 137 ms: 1.65x faster                                                         |
| raytrace                | 461 ms                                                 | 280 ms: 1.65x faster                                                         |
| chaos                   | 104 ms                                                 | 64.7 ms: 1.61x faster                                                        |
| crypto_pyaes            | 118 ms                                                 | 73.7 ms: 1.59x faster                                                        |
| hexiom                  | 9.42 ms                                                | 5.92 ms: 1.59x faster                                                        |
| spectral_norm           | 148 ms                                                 | 93.4 ms: 1.58x faster                                                        |
| scimark_monte_carlo     | 105 ms                                                 | 66.1 ms: 1.58x faster                                                        |
| pickle_pure_python      | 453 us                                                 | 287 us: 1.58x faster                                                         |
| python_startup          | 13.9 ms                                                | 8.88 ms: 1.57x faster                                                        |
| scimark_lu              | 158 ms                                                 | 105 ms: 1.51x faster                                                         |
| genshi_text             | 30.6 ms                                                | 20.6 ms: 1.48x faster                                                        |
| float                   | 108 ms                                                 | 72.7 ms: 1.48x faster                                                        |
| unpickle_pure_python    | 297 us                                                 | 202 us: 1.47x faster                                                         |
| deepcopy_memo           | 50.0 us                                                | 34.2 us: 1.46x faster                                                        |
| mako                    | 14.3 ms                                                | 9.75 ms: 1.46x faster                                                        |
| json_dumps              | 13.5 ms                                                | 9.33 ms: 1.44x faster                                                        |
| nbody                   | 136 ms                                                 | 94.4 ms: 1.44x faster                                                        |
| pprint_pformat          | 1.97 sec                                               | 1.38 sec: 1.43x faster                                                       |
| sqlglot_parse           | 2.04 ms                                                | 1.43 ms: 1.42x faster                                                        |
| django_template         | 46.3 ms                                                | 32.6 ms: 1.42x faster                                                        |
| sqlglot_transpile       | 2.42 ms                                                | 1.71 ms: 1.41x faster                                                        |
| logging_format          | 8.92 us                                                | 6.38 us: 1.40x faster                                                        |
| pprint_safe_repr        | 943 ms                                                 | 674 ms: 1.40x faster                                                         |
| html5lib                | 85.8 ms                                                | 61.4 ms: 1.40x faster                                                        |
| logging_simple          | 8.06 us                                                | 5.77 us: 1.40x faster                                                        |
| unpack_sequence         | 59.5 ns                                                | 43.0 ns: 1.38x faster                                                        |
| xml_etree_process       | 74.5 ms                                                | 54.0 ms: 1.38x faster                                                        |
| scimark_sparse_mat_mult | 5.48 ms                                                | 3.98 ms: 1.38x faster                                                        |
| genshi_xml              | 63.6 ms                                                | 46.3 ms: 1.37x faster                                                        |
| scimark_fft             | 414 ms                                                 | 302 ms: 1.37x faster                                                         |
| chameleon               | 8.86 ms                                                | 6.47 ms: 1.37x faster                                                        |
| thrift                  | 1.03 ms                                                | 758 us: 1.36x faster                                                         |
| async_tree_none         | 713 ms                                                 | 526 ms: 1.35x faster                                                         |
| regex_compile           | 174 ms                                                 | 128 ms: 1.35x faster                                                         |
| tornado_http            | 128 ms                                                 | 94.9 ms: 1.35x faster                                                        |
| aiohttp                 | 1.34 ms                                                | 996 us: 1.34x faster                                                         |
| deepcopy                | 429 us                                                 | 321 us: 1.34x faster                                                         |
| async_tree_memoization  | 854 ms                                                 | 641 ms: 1.33x faster                                                         |
| async_tree_io           | 1.78 sec                                               | 1.33 sec: 1.33x faster                                                       |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.33x faster                                                        |
| 2to3                    | 332 ms                                                 | 253 ms: 1.31x faster                                                         |
| pycparser               | 1.51 sec                                               | 1.15 sec: 1.31x faster                                                       |
| deepcopy_reduce         | 3.75 us                                                | 2.88 us: 1.30x faster                                                        |
| fannkuch                | 477 ms                                                 | 367 ms: 1.30x faster                                                         |
| nqueens                 | 99.3 ms                                                | 76.6 ms: 1.30x faster                                                        |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                         |
| sqlglot_optimize        | 65.3 ms                                                | 50.9 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed | 949 ms                                                 | 753 ms: 1.26x faster                                                         |
| docutils                | 3.18 sec                                               | 2.53 sec: 1.26x faster                                                       |
| mypy                    | 1.01 sec                                               | 809 ms: 1.25x faster                                                         |
| async_generators        | 428 ms                                                 | 353 ms: 1.21x faster                                                         |
| json_loads              | 28.9 us                                                | 23.9 us: 1.21x faster                                                        |
| sympy_integrate         | 23.9 ms                                                | 19.8 ms: 1.21x faster                                                        |
| bench_thread_pool       | 943 us                                                 | 781 us: 1.21x faster                                                         |
| dulwich_log             | 75.5 ms                                                | 62.8 ms: 1.20x faster                                                        |
| sympy_str               | 324 ms                                                 | 270 ms: 1.20x faster                                                         |
| coroutines              | 31.7 ms                                                | 26.4 ms: 1.20x faster                                                        |
| xml_etree_generate      | 93.3 ms                                                | 78.0 ms: 1.20x faster                                                        |
| sympy_expand            | 537 ms                                                 | 454 ms: 1.18x faster                                                         |
| sympy_sum               | 183 ms                                                 | 156 ms: 1.18x faster                                                         |
| json                    | 5.35 ms                                                | 4.64 ms: 1.15x faster                                                        |
| pathlib                 | 20.0 ms                                                | 17.6 ms: 1.14x faster                                                        |
| sqlite_synth            | 2.90 us                                                | 2.59 us: 1.12x faster                                                        |
| mdp                     | 2.82 sec                                               | 2.53 sec: 1.12x faster                                                       |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                         |
| regex_v8                | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                        |
| unpickle                | 14.3 us                                                | 13.0 us: 1.10x faster                                                        |
| meteor_contest          | 114 ms                                                 | 106 ms: 1.07x faster                                                         |
| pickle_list             | 4.50 us                                                | 4.31 us: 1.04x faster                                                        |
| telco                   | 6.68 ms                                                | 6.44 ms: 1.04x faster                                                        |
| xml_etree_iterparse     | 110 ms                                                 | 107 ms: 1.03x faster                                                         |
| pickle                  | 10.1 us                                                | 10.2 us: 1.01x slower                                                        |
| regex_dna               | 214 ms                                                 | 217 ms: 1.01x slower                                                         |
| generators              | 75.8 ms                                                | 77.3 ms: 1.02x slower                                                        |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                                         |
| python_startup_no_site  | 5.76 ms                                                | 6.43 ms: 1.12x slower                                                        |
| regex_effbot            | 3.21 ms                                                | 3.63 ms: 1.13x slower                                                        |
| pickle_dict             | 28.3 us                                                | 32.2 us: 1.14x slower                                                        |
| coverage                | 75.3 ms                                                | 100 ms: 1.33x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                 |

Benchmark hidden because not significant (2): bench_mp_pool, unpickle_list
Ignored benchmarks (4) of /home/mdboom/Work/builds/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230201-3.12.0a4+-49083fa/bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
