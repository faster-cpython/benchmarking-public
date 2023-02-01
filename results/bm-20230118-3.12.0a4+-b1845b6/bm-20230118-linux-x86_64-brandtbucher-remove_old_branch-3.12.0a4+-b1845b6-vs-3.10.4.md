
# Results vs. 3.10.4

- fork: brandtbucher
- ref: remove_old_branch
- machine: linux-x86_64
- commit hash: b1845b6
- commit date: 2023-01-18
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4+-b1845b6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 251 ms: 1.32x faster                                                      |
| chameleon      | 8.86 ms                                                | 6.42 ms: 1.38x faster                                                     |
| docutils       | 3.18 sec                                               | 2.51 sec: 1.27x faster                                                    |
| html5lib       | 85.8 ms                                                | 59.6 ms: 1.44x faster                                                     |
| tornado_http   | 128 ms                                                 | 93.4 ms: 1.37x faster                                                     |
| Geometric mean | (ref)                                                  | 1.36x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4+-b1845b6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 108 ms                                                 | 72.5 ms: 1.49x faster                                                     |
| nbody          | 136 ms                                                 | 92.8 ms: 1.47x faster                                                     |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                  | 1.29x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4+-b1845b6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 127 ms: 1.37x faster                                                      |
| regex_v8       | 25.0 ms                                                | 22.4 ms: 1.11x faster                                                     |
| regex_dna      | 214 ms                                                 | 210 ms: 1.02x faster                                                      |
| regex_effbot   | 3.21 ms                                                | 3.64 ms: 1.14x slower                                                     |
| Geometric mean | (ref)                                                  | 1.08x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4+-b1845b6 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 285 us: 1.59x faster                                                      |
| unpickle_pure_python | 297 us                                                 | 197 us: 1.50x faster                                                      |
| json_dumps           | 13.5 ms                                                | 9.42 ms: 1.43x faster                                                     |
| xml_etree_process    | 74.5 ms                                                | 54.1 ms: 1.38x faster                                                     |
| json_loads           | 28.9 us                                                | 23.9 us: 1.21x faster                                                     |
| xml_etree_generate   | 93.3 ms                                                | 77.9 ms: 1.20x faster                                                     |
| xml_etree_parse      | 163 ms                                                 | 151 ms: 1.08x faster                                                      |
| unpickle             | 14.3 us                                                | 13.4 us: 1.06x faster                                                     |
| pickle_list          | 4.50 us                                                | 4.27 us: 1.05x faster                                                     |
| xml_etree_iterparse  | 110 ms                                                 | 106 ms: 1.04x faster                                                      |
| pickle               | 10.1 us                                                | 10.2 us: 1.01x slower                                                     |
| pickle_dict          | 28.3 us                                                | 31.9 us: 1.12x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                              |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4+-b1845b6 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.96 ms: 1.55x faster                                                     |
| python_startup_no_site | 5.76 ms                                                | 6.48 ms: 1.12x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4+-b1845b6 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.6 ms: 1.48x faster                                                     |
| mako            | 14.3 ms                                                | 9.70 ms: 1.47x faster                                                     |
| django_template | 46.3 ms                                                | 32.4 ms: 1.43x faster                                                     |
| genshi_xml      | 63.6 ms                                                | 47.0 ms: 1.35x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                              |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4+-b1845b6 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.22 ms: 2.29x faster                                                     |
| logging_silent          | 173 ns                                                 | 91.6 ns: 1.89x faster                                                     |
| scimark_sor             | 193 ms                                                 | 106 ms: 1.83x faster                                                      |
| go                      | 226 ms                                                 | 133 ms: 1.71x faster                                                      |
| pyflate                 | 675 ms                                                 | 397 ms: 1.70x faster                                                      |
| richards                | 71.4 ms                                                | 42.1 ms: 1.70x faster                                                     |
| raytrace                | 461 ms                                                 | 283 ms: 1.63x faster                                                      |
| chaos                   | 104 ms                                                 | 64.3 ms: 1.62x faster                                                     |
| crypto_pyaes            | 118 ms                                                 | 72.6 ms: 1.62x faster                                                     |
| scimark_monte_carlo     | 105 ms                                                 | 65.1 ms: 1.61x faster                                                     |
| pickle_pure_python      | 453 us                                                 | 285 us: 1.59x faster                                                      |
| hexiom                  | 9.42 ms                                                | 6.02 ms: 1.56x faster                                                     |
| python_startup          | 13.9 ms                                                | 8.96 ms: 1.55x faster                                                     |
| spectral_norm           | 148 ms                                                 | 97.6 ms: 1.52x faster                                                     |
| unpickle_pure_python    | 297 us                                                 | 197 us: 1.50x faster                                                      |
| scimark_lu              | 158 ms                                                 | 106 ms: 1.49x faster                                                      |
| float                   | 108 ms                                                 | 72.5 ms: 1.49x faster                                                     |
| genshi_text             | 30.6 ms                                                | 20.6 ms: 1.48x faster                                                     |
| deepcopy_memo           | 50.0 us                                                | 33.9 us: 1.48x faster                                                     |
| mako                    | 14.3 ms                                                | 9.70 ms: 1.47x faster                                                     |
| nbody                   | 136 ms                                                 | 92.8 ms: 1.47x faster                                                     |
| html5lib                | 85.8 ms                                                | 59.6 ms: 1.44x faster                                                     |
| sqlglot_parse           | 2.04 ms                                                | 1.42 ms: 1.44x faster                                                     |
| json_dumps              | 13.5 ms                                                | 9.42 ms: 1.43x faster                                                     |
| django_template         | 46.3 ms                                                | 32.4 ms: 1.43x faster                                                     |
| unpack_sequence         | 59.5 ns                                                | 41.7 ns: 1.43x faster                                                     |
| sqlglot_transpile       | 2.42 ms                                                | 1.70 ms: 1.42x faster                                                     |
| pprint_pformat          | 1.97 sec                                               | 1.40 sec: 1.41x faster                                                    |
| logging_format          | 8.92 us                                                | 6.36 us: 1.40x faster                                                     |
| logging_simple          | 8.06 us                                                | 5.76 us: 1.40x faster                                                     |
| thrift                  | 1.03 ms                                                | 738 us: 1.40x faster                                                      |
| pprint_safe_repr        | 943 ms                                                 | 676 ms: 1.39x faster                                                      |
| chameleon               | 8.86 ms                                                | 6.42 ms: 1.38x faster                                                     |
| xml_etree_process       | 74.5 ms                                                | 54.1 ms: 1.38x faster                                                     |
| tornado_http            | 128 ms                                                 | 93.4 ms: 1.37x faster                                                     |
| async_tree_memoization  | 854 ms                                                 | 625 ms: 1.37x faster                                                      |
| scimark_fft             | 414 ms                                                 | 303 ms: 1.37x faster                                                      |
| regex_compile           | 174 ms                                                 | 127 ms: 1.37x faster                                                      |
| async_tree_none         | 713 ms                                                 | 524 ms: 1.36x faster                                                      |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.04 ms: 1.36x faster                                                     |
| genshi_xml              | 63.6 ms                                                | 47.0 ms: 1.35x faster                                                     |
| async_tree_io           | 1.78 sec                                               | 1.31 sec: 1.35x faster                                                    |
| aiohttp                 | 1.34 ms                                                | 996 us: 1.34x faster                                                      |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.33x faster                                                     |
| 2to3                    | 332 ms                                                 | 251 ms: 1.32x faster                                                      |
| pycparser               | 1.51 sec                                               | 1.14 sec: 1.32x faster                                                    |
| deepcopy                | 429 us                                                 | 326 us: 1.32x faster                                                      |
| fannkuch                | 477 ms                                                 | 362 ms: 1.32x faster                                                      |
| nqueens                 | 99.3 ms                                                | 76.7 ms: 1.29x faster                                                     |
| deepcopy_reduce         | 3.75 us                                                | 2.91 us: 1.29x faster                                                     |
| sqlglot_optimize        | 65.3 ms                                                | 50.9 ms: 1.28x faster                                                     |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.28x faster                                                      |
| coroutines              | 31.7 ms                                                | 24.8 ms: 1.28x faster                                                     |
| docutils                | 3.18 sec                                               | 2.51 sec: 1.27x faster                                                    |
| mypy                    | 1.01 sec                                               | 805 ms: 1.26x faster                                                      |
| async_tree_cpu_io_mixed | 949 ms                                                 | 757 ms: 1.25x faster                                                      |
| dulwich_log             | 75.5 ms                                                | 62.0 ms: 1.22x faster                                                     |
| bench_thread_pool       | 943 us                                                 | 774 us: 1.22x faster                                                      |
| sympy_integrate         | 23.9 ms                                                | 19.6 ms: 1.22x faster                                                     |
| sympy_str               | 324 ms                                                 | 268 ms: 1.21x faster                                                      |
| json_loads              | 28.9 us                                                | 23.9 us: 1.21x faster                                                     |
| async_generators        | 428 ms                                                 | 355 ms: 1.20x faster                                                      |
| xml_etree_generate      | 93.3 ms                                                | 77.9 ms: 1.20x faster                                                     |
| sympy_expand            | 537 ms                                                 | 451 ms: 1.19x faster                                                      |
| sympy_sum               | 183 ms                                                 | 155 ms: 1.19x faster                                                      |
| json                    | 5.35 ms                                                | 4.59 ms: 1.17x faster                                                     |
| regex_v8                | 25.0 ms                                                | 22.4 ms: 1.11x faster                                                     |
| sqlite_synth            | 2.90 us                                                | 2.61 us: 1.11x faster                                                     |
| pathlib                 | 20.0 ms                                                | 18.1 ms: 1.10x faster                                                     |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.10x faster                                                      |
| xml_etree_parse         | 163 ms                                                 | 151 ms: 1.08x faster                                                      |
| telco                   | 6.68 ms                                                | 6.26 ms: 1.07x faster                                                     |
| unpickle                | 14.3 us                                                | 13.4 us: 1.06x faster                                                     |
| pickle_list             | 4.50 us                                                | 4.27 us: 1.05x faster                                                     |
| mdp                     | 2.82 sec                                               | 2.69 sec: 1.05x faster                                                    |
| xml_etree_iterparse     | 110 ms                                                 | 106 ms: 1.04x faster                                                      |
| regex_dna               | 214 ms                                                 | 210 ms: 1.02x faster                                                      |
| pickle                  | 10.1 us                                                | 10.2 us: 1.01x slower                                                     |
| pidigits                | 190 ms                                                 | 192 ms: 1.01x slower                                                      |
| generators              | 75.8 ms                                                | 76.9 ms: 1.02x slower                                                     |
| pickle_dict             | 28.3 us                                                | 31.9 us: 1.12x slower                                                     |
| python_startup_no_site  | 5.76 ms                                                | 6.48 ms: 1.12x slower                                                     |
| regex_effbot            | 3.21 ms                                                | 3.64 ms: 1.14x slower                                                     |
| coverage                | 75.3 ms                                                | 97.0 ms: 1.29x slower                                                     |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                              |

Benchmark hidden because not significant (2): bench_mp_pool, unpickle_list
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230118-3.12.0a4+-b1845b6/bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4+-b1845b6.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
