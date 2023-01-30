
# Results vs. 3.10.4

- fork: iritkatriel
- ref: single_op_exit
- machine: linux-x86_64
- commit hash: 4684fa7
- commit date: 2023-01-27
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 251 ms: 1.32x faster                                                  |
| chameleon      | 8.86 ms                                                | 6.53 ms: 1.36x faster                                                 |
| docutils       | 3.18 sec                                               | 2.50 sec: 1.27x faster                                                |
| html5lib       | 85.8 ms                                                | 60.1 ms: 1.43x faster                                                 |
| tornado_http   | 128 ms                                                 | 93.0 ms: 1.38x faster                                                 |
| Geometric mean | (ref)                                                  | 1.35x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 108 ms                                                 | 72.8 ms: 1.48x faster                                                 |
| nbody          | 136 ms                                                 | 95.1 ms: 1.43x faster                                                 |
| pidigits       | 190 ms                                                 | 189 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.29x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 128 ms: 1.36x faster                                                  |
| regex_dna      | 214 ms                                                 | 209 ms: 1.02x faster                                                  |
| regex_v8       | 25.0 ms                                                | 25.9 ms: 1.04x slower                                                 |
| regex_effbot   | 3.21 ms                                                | 3.57 ms: 1.11x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 283 us: 1.60x faster                                                  |
| unpickle_pure_python | 297 us                                                 | 197 us: 1.51x faster                                                  |
| json_dumps           | 13.5 ms                                                | 9.28 ms: 1.45x faster                                                 |
| xml_etree_process    | 74.5 ms                                                | 54.1 ms: 1.38x faster                                                 |
| xml_etree_generate   | 93.3 ms                                                | 77.6 ms: 1.20x faster                                                 |
| json_loads           | 28.9 us                                                | 24.1 us: 1.20x faster                                                 |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                  |
| xml_etree_iterparse  | 110 ms                                                 | 102 ms: 1.08x faster                                                  |
| unpickle             | 14.3 us                                                | 13.3 us: 1.07x faster                                                 |
| pickle_list          | 4.50 us                                                | 4.21 us: 1.07x faster                                                 |
| pickle_dict          | 28.3 us                                                | 31.1 us: 1.10x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                          |

Benchmark hidden because not significant (2): unpickle_list, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.96 ms: 1.55x faster                                                 |
| python_startup_no_site | 5.76 ms                                                | 6.48 ms: 1.12x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.4 ms: 1.50x faster                                                 |
| mako            | 14.3 ms                                                | 9.69 ms: 1.47x faster                                                 |
| django_template | 46.3 ms                                                | 32.5 ms: 1.42x faster                                                 |
| genshi_xml      | 63.6 ms                                                | 46.1 ms: 1.38x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.26 ms: 2.27x faster                                                 |
| logging_silent          | 173 ns                                                 | 92.0 ns: 1.88x faster                                                 |
| scimark_sor             | 193 ms                                                 | 107 ms: 1.80x faster                                                  |
| richards                | 71.4 ms                                                | 42.1 ms: 1.70x faster                                                 |
| pyflate                 | 675 ms                                                 | 399 ms: 1.69x faster                                                  |
| go                      | 226 ms                                                 | 137 ms: 1.66x faster                                                  |
| raytrace                | 461 ms                                                 | 281 ms: 1.64x faster                                                  |
| scimark_monte_carlo     | 105 ms                                                 | 64.2 ms: 1.63x faster                                                 |
| chaos                   | 104 ms                                                 | 64.8 ms: 1.61x faster                                                 |
| crypto_pyaes            | 118 ms                                                 | 73.3 ms: 1.60x faster                                                 |
| pickle_pure_python      | 453 us                                                 | 283 us: 1.60x faster                                                  |
| hexiom                  | 9.42 ms                                                | 5.94 ms: 1.59x faster                                                 |
| python_startup          | 13.9 ms                                                | 8.96 ms: 1.55x faster                                                 |
| spectral_norm           | 148 ms                                                 | 96.5 ms: 1.54x faster                                                 |
| unpickle_pure_python    | 297 us                                                 | 197 us: 1.51x faster                                                  |
| genshi_text             | 30.6 ms                                                | 20.4 ms: 1.50x faster                                                 |
| scimark_lu              | 158 ms                                                 | 106 ms: 1.49x faster                                                  |
| float                   | 108 ms                                                 | 72.8 ms: 1.48x faster                                                 |
| mako                    | 14.3 ms                                                | 9.69 ms: 1.47x faster                                                 |
| json_dumps              | 13.5 ms                                                | 9.28 ms: 1.45x faster                                                 |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.44x faster                                                 |
| deepcopy_memo           | 50.0 us                                                | 34.7 us: 1.44x faster                                                 |
| nbody                   | 136 ms                                                 | 95.1 ms: 1.43x faster                                                 |
| logging_format          | 8.92 us                                                | 6.25 us: 1.43x faster                                                 |
| pprint_pformat          | 1.97 sec                                               | 1.38 sec: 1.43x faster                                                |
| html5lib                | 85.8 ms                                                | 60.1 ms: 1.43x faster                                                 |
| django_template         | 46.3 ms                                                | 32.5 ms: 1.42x faster                                                 |
| sqlglot_transpile       | 2.42 ms                                                | 1.71 ms: 1.41x faster                                                 |
| logging_simple          | 8.06 us                                                | 5.70 us: 1.41x faster                                                 |
| pprint_safe_repr        | 943 ms                                                 | 674 ms: 1.40x faster                                                  |
| unpack_sequence         | 59.5 ns                                                | 42.8 ns: 1.39x faster                                                 |
| pycparser               | 1.51 sec                                               | 1.09 sec: 1.38x faster                                                |
| genshi_xml              | 63.6 ms                                                | 46.1 ms: 1.38x faster                                                 |
| tornado_http            | 128 ms                                                 | 93.0 ms: 1.38x faster                                                 |
| xml_etree_process       | 74.5 ms                                                | 54.1 ms: 1.38x faster                                                 |
| scimark_sparse_mat_mult | 5.48 ms                                                | 3.99 ms: 1.37x faster                                                 |
| scimark_fft             | 414 ms                                                 | 301 ms: 1.37x faster                                                  |
| thrift                  | 1.03 ms                                                | 755 us: 1.37x faster                                                  |
| regex_compile           | 174 ms                                                 | 128 ms: 1.36x faster                                                  |
| async_tree_none         | 713 ms                                                 | 525 ms: 1.36x faster                                                  |
| gunicorn                | 1.43 ms                                                | 1.06 ms: 1.36x faster                                                 |
| chameleon               | 8.86 ms                                                | 6.53 ms: 1.36x faster                                                 |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                                |
| async_tree_memoization  | 854 ms                                                 | 633 ms: 1.35x faster                                                  |
| aiohttp                 | 1.34 ms                                                | 991 us: 1.35x faster                                                  |
| 2to3                    | 332 ms                                                 | 251 ms: 1.32x faster                                                  |
| deepcopy                | 429 us                                                 | 327 us: 1.31x faster                                                  |
| nqueens                 | 99.3 ms                                                | 76.8 ms: 1.29x faster                                                 |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.29x faster                                                  |
| sqlglot_optimize        | 65.3 ms                                                | 50.6 ms: 1.29x faster                                                 |
| deepcopy_reduce         | 3.75 us                                                | 2.93 us: 1.28x faster                                                 |
| coroutines              | 31.7 ms                                                | 24.8 ms: 1.27x faster                                                 |
| docutils                | 3.18 sec                                               | 2.50 sec: 1.27x faster                                                |
| fannkuch                | 477 ms                                                 | 377 ms: 1.27x faster                                                  |
| mypy                    | 1.01 sec                                               | 802 ms: 1.26x faster                                                  |
| async_tree_cpu_io_mixed | 949 ms                                                 | 757 ms: 1.25x faster                                                  |
| bench_thread_pool       | 943 us                                                 | 769 us: 1.23x faster                                                  |
| dulwich_log             | 75.5 ms                                                | 61.8 ms: 1.22x faster                                                 |
| sympy_integrate         | 23.9 ms                                                | 19.7 ms: 1.22x faster                                                 |
| sympy_str               | 324 ms                                                 | 268 ms: 1.21x faster                                                  |
| async_generators        | 428 ms                                                 | 354 ms: 1.21x faster                                                  |
| xml_etree_generate      | 93.3 ms                                                | 77.6 ms: 1.20x faster                                                 |
| json_loads              | 28.9 us                                                | 24.1 us: 1.20x faster                                                 |
| sympy_expand            | 537 ms                                                 | 452 ms: 1.19x faster                                                  |
| sympy_sum               | 183 ms                                                 | 154 ms: 1.19x faster                                                  |
| json                    | 5.35 ms                                                | 4.61 ms: 1.16x faster                                                 |
| sqlite_synth            | 2.90 us                                                | 2.57 us: 1.13x faster                                                 |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.13x faster                                                 |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                  |
| xml_etree_iterparse     | 110 ms                                                 | 102 ms: 1.08x faster                                                  |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.08x faster                                                  |
| unpickle                | 14.3 us                                                | 13.3 us: 1.07x faster                                                 |
| pickle_list             | 4.50 us                                                | 4.21 us: 1.07x faster                                                 |
| telco                   | 6.68 ms                                                | 6.28 ms: 1.06x faster                                                 |
| mdp                     | 2.82 sec                                               | 2.69 sec: 1.05x faster                                                |
| regex_dna               | 214 ms                                                 | 209 ms: 1.02x faster                                                  |
| generators              | 75.8 ms                                                | 74.9 ms: 1.01x faster                                                 |
| pidigits                | 190 ms                                                 | 189 ms: 1.01x faster                                                  |
| regex_v8                | 25.0 ms                                                | 25.9 ms: 1.04x slower                                                 |
| pickle_dict             | 28.3 us                                                | 31.1 us: 1.10x slower                                                 |
| regex_effbot            | 3.21 ms                                                | 3.57 ms: 1.11x slower                                                 |
| python_startup_no_site  | 5.76 ms                                                | 6.48 ms: 1.12x slower                                                 |
| coverage                | 75.3 ms                                                | 97.8 ms: 1.30x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                          |

Benchmark hidden because not significant (3): unpickle_list, pickle, bench_mp_pool
Ignored benchmarks (4) of /home/mdboom/Work/builds/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230127-3.12.0a4+-4684fa7/bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
