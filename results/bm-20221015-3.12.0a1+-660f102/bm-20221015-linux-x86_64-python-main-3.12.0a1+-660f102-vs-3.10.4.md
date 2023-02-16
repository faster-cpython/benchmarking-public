
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 660f102
- commit date: 2022-10-15
- overall geometric mean: 1.31x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221015-linux-x86_64-python-main-3.12.0a1+-660f102 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 249 ms: 1.35x faster                                   |
| chameleon      | 9.17 ms                                                | 6.71 ms: 1.37x faster                                  |
| html5lib       | 85.9 ms                                                | 59.2 ms: 1.45x faster                                  |
| tornado_http   | 128 ms                                                 | 92.6 ms: 1.38x faster                                  |
| Geometric mean | (ref)                                                  | 1.39x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221015-linux-x86_64-python-main-3.12.0a1+-660f102 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 144 ms                                                 | 94.2 ms: 1.53x faster                                  |
| float          | 109 ms                                                 | 72.2 ms: 1.51x faster                                  |
| pidigits       | 190 ms                                                 | 199 ms: 1.05x slower                                   |
| Geometric mean | (ref)                                                  | 1.30x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221015-linux-x86_64-python-main-3.12.0a1+-660f102 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.37x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.2 ms: 1.13x faster                                  |
| regex_dna      | 214 ms                                                 | 200 ms: 1.07x faster                                   |
| regex_effbot   | 3.19 ms                                                | 3.60 ms: 1.13x slower                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221015-linux-x86_64-python-main-3.12.0a1+-660f102 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 293 us: 1.54x faster                                   |
| unpickle_pure_python | 302 us                                                 | 202 us: 1.49x faster                                   |
| json_dumps           | 13.4 ms                                                | 9.60 ms: 1.40x faster                                  |
| xml_etree_process    | 74.5 ms                                                | 53.7 ms: 1.39x faster                                  |
| xml_etree_generate   | 93.8 ms                                                | 76.9 ms: 1.22x faster                                  |
| json_loads           | 28.7 us                                                | 23.9 us: 1.20x faster                                  |
| pickle_list          | 4.72 us                                                | 4.14 us: 1.14x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 145 ms: 1.12x faster                                   |
| unpickle             | 14.2 us                                                | 12.9 us: 1.10x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                   |
| unpickle_list        | 4.92 us                                                | 4.96 us: 1.01x slower                                  |
| pickle               | 10.2 us                                                | 10.3 us: 1.01x slower                                  |
| pickle_dict          | 27.6 us                                                | 31.1 us: 1.13x slower                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221015-linux-x86_64-python-main-3.12.0a1+-660f102 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.41 ms: 1.67x faster                                  |
| python_startup_no_site | 5.78 ms                                                | 6.09 ms: 1.05x slower                                  |
| Geometric mean         | (ref)                                                  | 1.26x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221015-linux-x86_64-python-main-3.12.0a1+-660f102 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.82 ms: 1.49x faster                                  |
| genshi_text     | 30.6 ms                                                | 21.0 ms: 1.46x faster                                  |
| django_template | 46.3 ms                                                | 32.6 ms: 1.42x faster                                  |
| genshi_xml      | 63.7 ms                                                | 49.2 ms: 1.29x faster                                  |
| Geometric mean  | (ref)                                                  | 1.41x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221015-linux-x86_64-python-main-3.12.0a1+-660f102 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.31 ms: 2.20x faster                                  |
| logging_silent          | 176 ns                                                 | 92.9 ns: 1.90x faster                                  |
| scimark_sor             | 197 ms                                                 | 104 ms: 1.90x faster                                   |
| richards                | 75.2 ms                                                | 43.0 ms: 1.75x faster                                  |
| go                      | 226 ms                                                 | 134 ms: 1.69x faster                                   |
| pyflate                 | 676 ms                                                 | 402 ms: 1.68x faster                                   |
| python_startup          | 14.1 ms                                                | 8.41 ms: 1.67x faster                                  |
| scimark_monte_carlo     | 109 ms                                                 | 65.6 ms: 1.65x faster                                  |
| raytrace                | 467 ms                                                 | 285 ms: 1.64x faster                                   |
| chaos                   | 106 ms                                                 | 66.1 ms: 1.60x faster                                  |
| hexiom                  | 9.43 ms                                                | 6.05 ms: 1.56x faster                                  |
| crypto_pyaes            | 117 ms                                                 | 75.2 ms: 1.55x faster                                  |
| spectral_norm           | 150 ms                                                 | 96.7 ms: 1.55x faster                                  |
| pickle_pure_python      | 452 us                                                 | 293 us: 1.54x faster                                   |
| nbody                   | 144 ms                                                 | 94.2 ms: 1.53x faster                                  |
| sqlglot_parse           | 2.04 ms                                                | 1.34 ms: 1.52x faster                                  |
| float                   | 109 ms                                                 | 72.2 ms: 1.51x faster                                  |
| unpickle_pure_python    | 302 us                                                 | 202 us: 1.49x faster                                   |
| mako                    | 14.7 ms                                                | 9.82 ms: 1.49x faster                                  |
| sqlglot_transpile       | 2.43 ms                                                | 1.63 ms: 1.49x faster                                  |
| deepcopy_memo           | 51.7 us                                                | 34.6 us: 1.49x faster                                  |
| scimark_lu              | 161 ms                                                 | 108 ms: 1.49x faster                                   |
| genshi_text             | 30.6 ms                                                | 21.0 ms: 1.46x faster                                  |
| html5lib                | 85.9 ms                                                | 59.2 ms: 1.45x faster                                  |
| pprint_pformat          | 1.98 sec                                               | 1.37 sec: 1.44x faster                                 |
| pprint_safe_repr        | 953 ms                                                 | 669 ms: 1.43x faster                                   |
| django_template         | 46.3 ms                                                | 32.6 ms: 1.42x faster                                  |
| logging_simple          | 8.10 us                                                | 5.73 us: 1.41x faster                                  |
| json_dumps              | 13.4 ms                                                | 9.60 ms: 1.40x faster                                  |
| pycparser               | 1.53 sec                                               | 1.10 sec: 1.40x faster                                 |
| thrift                  | 1.03 ms                                                | 742 us: 1.39x faster                                   |
| logging_format          | 8.85 us                                                | 6.38 us: 1.39x faster                                  |
| xml_etree_process       | 74.5 ms                                                | 53.7 ms: 1.39x faster                                  |
| tornado_http            | 128 ms                                                 | 92.6 ms: 1.38x faster                                  |
| regex_compile           | 177 ms                                                 | 129 ms: 1.37x faster                                   |
| chameleon               | 9.17 ms                                                | 6.71 ms: 1.37x faster                                  |
| 2to3                    | 335 ms                                                 | 249 ms: 1.35x faster                                   |
| unpack_sequence         | 59.4 ns                                                | 44.1 ns: 1.35x faster                                  |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                 |
| aiohttp                 | 1.34 ms                                                | 997 us: 1.34x faster                                   |
| scimark_fft             | 421 ms                                                 | 315 ms: 1.33x faster                                   |
| async_tree_none         | 711 ms                                                 | 533 ms: 1.33x faster                                   |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.33x faster                                  |
| fannkuch                | 488 ms                                                 | 368 ms: 1.32x faster                                   |
| async_tree_memoization  | 855 ms                                                 | 647 ms: 1.32x faster                                   |
| deepcopy                | 438 us                                                 | 332 us: 1.32x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.16 ms: 1.31x faster                                  |
| deepcopy_reduce         | 3.79 us                                                | 2.91 us: 1.30x faster                                  |
| async_tree_cpu_io_mixed | 949 ms                                                 | 730 ms: 1.30x faster                                   |
| genshi_xml              | 63.7 ms                                                | 49.2 ms: 1.29x faster                                  |
| coroutines              | 31.6 ms                                                | 24.6 ms: 1.29x faster                                  |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.28x faster                                   |
| sqlglot_optimize        | 65.2 ms                                                | 51.5 ms: 1.27x faster                                  |
| nqueens                 | 100 ms                                                 | 79.5 ms: 1.26x faster                                  |
| dulwich_log             | 75.8 ms                                                | 60.9 ms: 1.25x faster                                  |
| xml_etree_generate      | 93.8 ms                                                | 76.9 ms: 1.22x faster                                  |
| json_loads              | 28.7 us                                                | 23.9 us: 1.20x faster                                  |
| sympy_integrate         | 24.0 ms                                                | 20.4 ms: 1.18x faster                                  |
| pylint                  | 532 ms                                                 | 455 ms: 1.17x faster                                   |
| sympy_expand            | 534 ms                                                 | 458 ms: 1.17x faster                                   |
| sympy_str               | 325 ms                                                 | 281 ms: 1.16x faster                                   |
| pickle_list             | 4.72 us                                                | 4.14 us: 1.14x faster                                  |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                  |
| regex_v8                | 25.0 ms                                                | 22.2 ms: 1.13x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 145 ms: 1.12x faster                                   |
| sympy_sum               | 183 ms                                                 | 163 ms: 1.12x faster                                   |
| json                    | 5.35 ms                                                | 4.78 ms: 1.12x faster                                  |
| sqlite_synth            | 2.92 us                                                | 2.62 us: 1.12x faster                                  |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.10x faster                                   |
| unpickle                | 14.2 us                                                | 12.9 us: 1.10x faster                                  |
| mdp                     | 2.74 sec                                               | 2.54 sec: 1.08x faster                                 |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                   |
| regex_dna               | 214 ms                                                 | 200 ms: 1.07x faster                                   |
| generators              | 76.4 ms                                                | 71.8 ms: 1.06x faster                                  |
| telco                   | 6.73 ms                                                | 6.46 ms: 1.04x faster                                  |
| unpickle_list           | 4.92 us                                                | 4.96 us: 1.01x slower                                  |
| pickle                  | 10.2 us                                                | 10.3 us: 1.01x slower                                  |
| pidigits                | 190 ms                                                 | 199 ms: 1.05x slower                                   |
| python_startup_no_site  | 5.78 ms                                                | 6.09 ms: 1.05x slower                                  |
| pickle_dict             | 27.6 us                                                | 31.1 us: 1.13x slower                                  |
| regex_effbot            | 3.19 ms                                                | 3.60 ms: 1.13x slower                                  |
| coverage                | 74.7 ms                                                | 98.4 ms: 1.32x slower                                  |
| Geometric mean          | (ref)                                                  | 1.31x faster                                           |
Ignored benchmarks (13) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: async_generators, asyncio_tcp, bench_mp_pool, bench_thread_pool, create_gc_cycles, dask, djangocms, docutils, flaskblogging, gc_traversal, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221015-3.12.0a1+-660f102/bm-20221015-linux-x86_64-python-main-3.12.0a1+-660f102.json: mypy
