
# Results vs. 3.10.4

- fork: brandtbucher
- ref: compare_and_not_bran
- machine: linux-x86_64
- commit hash: 49083fa
- commit date: 2023-02-01
- overall geometric mean: 1.29x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 253 ms: 1.32x faster                                                         |
| chameleon      | 8.86 ms                                                | 6.50 ms: 1.36x faster                                                        |
| docutils       | 3.18 sec                                               | 2.53 sec: 1.26x faster                                                       |
| html5lib       | 85.8 ms                                                | 61.0 ms: 1.41x faster                                                        |
| tornado_http   | 128 ms                                                 | 94.6 ms: 1.36x faster                                                        |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 108 ms                                                 | 73.8 ms: 1.46x faster                                                        |
| nbody          | 136 ms                                                 | 93.3 ms: 1.46x faster                                                        |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                                         |
| Geometric mean | (ref)                                                  | 1.27x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 134 ms: 1.30x faster                                                         |
| regex_v8       | 25.0 ms                                                | 22.6 ms: 1.11x faster                                                        |
| regex_dna      | 214 ms                                                 | 209 ms: 1.02x faster                                                         |
| regex_effbot   | 3.21 ms                                                | 3.54 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 290 us: 1.56x faster                                                         |
| unpickle_pure_python | 297 us                                                 | 203 us: 1.46x faster                                                         |
| json_dumps           | 13.5 ms                                                | 9.41 ms: 1.43x faster                                                        |
| xml_etree_process    | 74.5 ms                                                | 53.5 ms: 1.39x faster                                                        |
| xml_etree_generate   | 93.3 ms                                                | 77.5 ms: 1.20x faster                                                        |
| json_loads           | 28.9 us                                                | 24.3 us: 1.19x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 151 ms: 1.08x faster                                                         |
| unpickle             | 14.3 us                                                | 13.3 us: 1.07x faster                                                        |
| pickle_list          | 4.50 us                                                | 4.26 us: 1.06x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                 | 106 ms: 1.04x faster                                                         |
| pickle               | 10.1 us                                                | 10.3 us: 1.02x slower                                                        |
| pickle_dict          | 28.3 us                                                | 32.1 us: 1.14x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                                 |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.94 ms: 1.56x faster                                                        |
| python_startup_no_site | 5.76 ms                                                | 6.46 ms: 1.12x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.7 ms: 1.48x faster                                                        |
| mako            | 14.3 ms                                                | 9.78 ms: 1.46x faster                                                        |
| django_template | 46.3 ms                                                | 33.4 ms: 1.39x faster                                                        |
| genshi_xml      | 63.6 ms                                                | 47.5 ms: 1.34x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.28 ms: 2.26x faster                                                        |
| logging_silent          | 173 ns                                                 | 95.5 ns: 1.81x faster                                                        |
| scimark_sor             | 193 ms                                                 | 109 ms: 1.77x faster                                                         |
| pyflate                 | 675 ms                                                 | 407 ms: 1.66x faster                                                         |
| richards                | 71.4 ms                                                | 43.0 ms: 1.66x faster                                                        |
| raytrace                | 461 ms                                                 | 281 ms: 1.64x faster                                                         |
| go                      | 226 ms                                                 | 139 ms: 1.63x faster                                                         |
| crypto_pyaes            | 118 ms                                                 | 72.8 ms: 1.61x faster                                                        |
| hexiom                  | 9.42 ms                                                | 5.89 ms: 1.60x faster                                                        |
| chaos                   | 104 ms                                                 | 66.1 ms: 1.58x faster                                                        |
| scimark_monte_carlo     | 105 ms                                                 | 67.0 ms: 1.56x faster                                                        |
| pickle_pure_python      | 453 us                                                 | 290 us: 1.56x faster                                                         |
| python_startup          | 13.9 ms                                                | 8.94 ms: 1.56x faster                                                        |
| spectral_norm           | 148 ms                                                 | 95.2 ms: 1.56x faster                                                        |
| scimark_lu              | 158 ms                                                 | 105 ms: 1.50x faster                                                         |
| genshi_text             | 30.6 ms                                                | 20.7 ms: 1.48x faster                                                        |
| float                   | 108 ms                                                 | 73.8 ms: 1.46x faster                                                        |
| unpickle_pure_python    | 297 us                                                 | 203 us: 1.46x faster                                                         |
| nbody                   | 136 ms                                                 | 93.3 ms: 1.46x faster                                                        |
| mako                    | 14.3 ms                                                | 9.78 ms: 1.46x faster                                                        |
| json_dumps              | 13.5 ms                                                | 9.41 ms: 1.43x faster                                                        |
| deepcopy_memo           | 50.0 us                                                | 34.9 us: 1.43x faster                                                        |
| unpack_sequence         | 59.5 ns                                                | 42.0 ns: 1.41x faster                                                        |
| sqlglot_parse           | 2.04 ms                                                | 1.44 ms: 1.41x faster                                                        |
| html5lib                | 85.8 ms                                                | 61.0 ms: 1.41x faster                                                        |
| pprint_pformat          | 1.97 sec                                               | 1.41 sec: 1.40x faster                                                       |
| sqlglot_transpile       | 2.42 ms                                                | 1.73 ms: 1.40x faster                                                        |
| logging_format          | 8.92 us                                                | 6.40 us: 1.39x faster                                                        |
| xml_etree_process       | 74.5 ms                                                | 53.5 ms: 1.39x faster                                                        |
| logging_simple          | 8.06 us                                                | 5.80 us: 1.39x faster                                                        |
| django_template         | 46.3 ms                                                | 33.4 ms: 1.39x faster                                                        |
| pprint_safe_repr        | 943 ms                                                 | 681 ms: 1.38x faster                                                         |
| thrift                  | 1.03 ms                                                | 756 us: 1.36x faster                                                         |
| chameleon               | 8.86 ms                                                | 6.50 ms: 1.36x faster                                                        |
| async_tree_io           | 1.78 sec                                               | 1.31 sec: 1.36x faster                                                       |
| scimark_fft             | 414 ms                                                 | 305 ms: 1.36x faster                                                         |
| async_tree_none         | 713 ms                                                 | 526 ms: 1.36x faster                                                         |
| tornado_http            | 128 ms                                                 | 94.6 ms: 1.36x faster                                                        |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.07 ms: 1.35x faster                                                        |
| aiohttp                 | 1.34 ms                                                | 997 us: 1.34x faster                                                         |
| genshi_xml              | 63.6 ms                                                | 47.5 ms: 1.34x faster                                                        |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.33x faster                                                        |
| async_tree_memoization  | 854 ms                                                 | 642 ms: 1.33x faster                                                         |
| 2to3                    | 332 ms                                                 | 253 ms: 1.32x faster                                                         |
| fannkuch                | 477 ms                                                 | 364 ms: 1.31x faster                                                         |
| pycparser               | 1.51 sec                                               | 1.16 sec: 1.31x faster                                                       |
| regex_compile           | 174 ms                                                 | 134 ms: 1.30x faster                                                         |
| nqueens                 | 99.3 ms                                                | 76.6 ms: 1.30x faster                                                        |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.29x faster                                                         |
| deepcopy                | 429 us                                                 | 333 us: 1.29x faster                                                         |
| deepcopy_reduce         | 3.75 us                                                | 2.91 us: 1.29x faster                                                        |
| sqlglot_optimize        | 65.3 ms                                                | 50.8 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed | 949 ms                                                 | 750 ms: 1.26x faster                                                         |
| docutils                | 3.18 sec                                               | 2.53 sec: 1.26x faster                                                       |
| mypy                    | 1.01 sec                                               | 807 ms: 1.26x faster                                                         |
| coroutines              | 31.7 ms                                                | 25.3 ms: 1.25x faster                                                        |
| async_generators        | 428 ms                                                 | 351 ms: 1.22x faster                                                         |
| bench_thread_pool       | 943 us                                                 | 779 us: 1.21x faster                                                         |
| dulwich_log             | 75.5 ms                                                | 62.4 ms: 1.21x faster                                                        |
| sympy_integrate         | 23.9 ms                                                | 19.8 ms: 1.21x faster                                                        |
| sympy_str               | 324 ms                                                 | 269 ms: 1.21x faster                                                         |
| xml_etree_generate      | 93.3 ms                                                | 77.5 ms: 1.20x faster                                                        |
| json_loads              | 28.9 us                                                | 24.3 us: 1.19x faster                                                        |
| sympy_expand            | 537 ms                                                 | 454 ms: 1.18x faster                                                         |
| sympy_sum               | 183 ms                                                 | 155 ms: 1.18x faster                                                         |
| json                    | 5.35 ms                                                | 4.69 ms: 1.14x faster                                                        |
| sqlite_synth            | 2.90 us                                                | 2.58 us: 1.12x faster                                                        |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                                        |
| regex_v8                | 25.0 ms                                                | 22.6 ms: 1.11x faster                                                        |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.10x faster                                                         |
| xml_etree_parse         | 163 ms                                                 | 151 ms: 1.08x faster                                                         |
| unpickle                | 14.3 us                                                | 13.3 us: 1.07x faster                                                        |
| pickle_list             | 4.50 us                                                | 4.26 us: 1.06x faster                                                        |
| mdp                     | 2.82 sec                                               | 2.68 sec: 1.05x faster                                                       |
| xml_etree_iterparse     | 110 ms                                                 | 106 ms: 1.04x faster                                                         |
| telco                   | 6.68 ms                                                | 6.52 ms: 1.02x faster                                                        |
| regex_dna               | 214 ms                                                 | 209 ms: 1.02x faster                                                         |
| generators              | 75.8 ms                                                | 75.4 ms: 1.00x faster                                                        |
| pickle                  | 10.1 us                                                | 10.3 us: 1.02x slower                                                        |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                                         |
| regex_effbot            | 3.21 ms                                                | 3.54 ms: 1.10x slower                                                        |
| python_startup_no_site  | 5.76 ms                                                | 6.46 ms: 1.12x slower                                                        |
| pickle_dict             | 28.3 us                                                | 32.1 us: 1.14x slower                                                        |
| coverage                | 75.3 ms                                                | 98.3 ms: 1.31x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                                 |

Benchmark hidden because not significant (2): unpickle_list, bench_mp_pool
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230201-3.12.0a4+-49083fa/bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
