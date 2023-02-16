
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 2d2e01a
- commit date: 2022-10-09
- overall geometric mean: 1.31x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221009-linux-x86_64-python-main-3.12.0a1+-2d2e01a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 248 ms: 1.35x faster                                   |
| chameleon      | 9.17 ms                                                | 6.61 ms: 1.39x faster                                  |
| html5lib       | 85.9 ms                                                | 59.7 ms: 1.44x faster                                  |
| tornado_http   | 128 ms                                                 | 93.4 ms: 1.37x faster                                  |
| Geometric mean | (ref)                                                  | 1.39x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221009-linux-x86_64-python-main-3.12.0a1+-2d2e01a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 144 ms                                                 | 94.6 ms: 1.52x faster                                  |
| float          | 109 ms                                                 | 72.3 ms: 1.51x faster                                  |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.32x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221009-linux-x86_64-python-main-3.12.0a1+-2d2e01a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.39x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.1 ms: 1.13x faster                                  |
| regex_dna      | 214 ms                                                 | 203 ms: 1.05x faster                                   |
| regex_effbot   | 3.19 ms                                                | 3.60 ms: 1.13x slower                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221009-linux-x86_64-python-main-3.12.0a1+-2d2e01a |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 293 us: 1.54x faster                                   |
| unpickle_pure_python | 302 us                                                 | 204 us: 1.48x faster                                   |
| json_dumps           | 13.4 ms                                                | 9.44 ms: 1.42x faster                                  |
| xml_etree_process    | 74.5 ms                                                | 53.7 ms: 1.39x faster                                  |
| xml_etree_generate   | 93.8 ms                                                | 76.6 ms: 1.22x faster                                  |
| json_loads           | 28.7 us                                                | 23.8 us: 1.21x faster                                  |
| pickle_list          | 4.72 us                                                | 4.06 us: 1.16x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 146 ms: 1.12x faster                                   |
| xml_etree_iterparse  | 111 ms                                                 | 101 ms: 1.10x faster                                   |
| unpickle             | 14.2 us                                                | 13.0 us: 1.09x faster                                  |
| pickle               | 10.2 us                                                | 10.3 us: 1.01x slower                                  |
| unpickle_list        | 4.92 us                                                | 5.02 us: 1.02x slower                                  |
| pickle_dict          | 27.6 us                                                | 31.9 us: 1.16x slower                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221009-linux-x86_64-python-main-3.12.0a1+-2d2e01a |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.38 ms: 1.68x faster                                  |
| python_startup_no_site | 5.78 ms                                                | 6.06 ms: 1.05x slower                                  |
| Geometric mean         | (ref)                                                  | 1.27x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221009-linux-x86_64-python-main-3.12.0a1+-2d2e01a |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.84 ms: 1.49x faster                                  |
| genshi_text     | 30.6 ms                                                | 21.8 ms: 1.40x faster                                  |
| django_template | 46.3 ms                                                | 33.3 ms: 1.39x faster                                  |
| genshi_xml      | 63.7 ms                                                | 49.1 ms: 1.30x faster                                  |
| Geometric mean  | (ref)                                                  | 1.39x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221009-linux-x86_64-python-main-3.12.0a1+-2d2e01a |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.40 ms: 2.14x faster                                  |
| logging_silent          | 176 ns                                                 | 92.7 ns: 1.90x faster                                  |
| scimark_sor             | 197 ms                                                 | 105 ms: 1.88x faster                                   |
| richards                | 75.2 ms                                                | 44.4 ms: 1.69x faster                                  |
| python_startup          | 14.1 ms                                                | 8.38 ms: 1.68x faster                                  |
| pyflate                 | 676 ms                                                 | 407 ms: 1.66x faster                                   |
| raytrace                | 467 ms                                                 | 284 ms: 1.64x faster                                   |
| scimark_monte_carlo     | 109 ms                                                 | 66.3 ms: 1.64x faster                                  |
| go                      | 226 ms                                                 | 138 ms: 1.64x faster                                   |
| chaos                   | 106 ms                                                 | 65.5 ms: 1.61x faster                                  |
| hexiom                  | 9.43 ms                                                | 6.02 ms: 1.57x faster                                  |
| spectral_norm           | 150 ms                                                 | 96.4 ms: 1.55x faster                                  |
| crypto_pyaes            | 117 ms                                                 | 75.3 ms: 1.55x faster                                  |
| pickle_pure_python      | 452 us                                                 | 293 us: 1.54x faster                                   |
| sqlglot_parse           | 2.04 ms                                                | 1.34 ms: 1.52x faster                                  |
| nbody                   | 144 ms                                                 | 94.6 ms: 1.52x faster                                  |
| float                   | 109 ms                                                 | 72.3 ms: 1.51x faster                                  |
| deepcopy_memo           | 51.7 us                                                | 34.3 us: 1.50x faster                                  |
| mako                    | 14.7 ms                                                | 9.84 ms: 1.49x faster                                  |
| scimark_lu              | 161 ms                                                 | 108 ms: 1.49x faster                                   |
| unpickle_pure_python    | 302 us                                                 | 204 us: 1.48x faster                                   |
| sqlglot_transpile       | 2.43 ms                                                | 1.64 ms: 1.48x faster                                  |
| html5lib                | 85.9 ms                                                | 59.7 ms: 1.44x faster                                  |
| json_dumps              | 13.4 ms                                                | 9.44 ms: 1.42x faster                                  |
| pprint_pformat          | 1.98 sec                                               | 1.40 sec: 1.42x faster                                 |
| logging_simple          | 8.10 us                                                | 5.74 us: 1.41x faster                                  |
| pycparser               | 1.53 sec                                               | 1.09 sec: 1.41x faster                                 |
| thrift                  | 1.03 ms                                                | 737 us: 1.40x faster                                   |
| genshi_text             | 30.6 ms                                                | 21.8 ms: 1.40x faster                                  |
| pprint_safe_repr        | 953 ms                                                 | 682 ms: 1.40x faster                                   |
| django_template         | 46.3 ms                                                | 33.3 ms: 1.39x faster                                  |
| xml_etree_process       | 74.5 ms                                                | 53.7 ms: 1.39x faster                                  |
| regex_compile           | 177 ms                                                 | 128 ms: 1.39x faster                                   |
| chameleon               | 9.17 ms                                                | 6.61 ms: 1.39x faster                                  |
| logging_format          | 8.85 us                                                | 6.43 us: 1.38x faster                                  |
| tornado_http            | 128 ms                                                 | 93.4 ms: 1.37x faster                                  |
| async_tree_io           | 1.78 sec                                               | 1.31 sec: 1.35x faster                                 |
| 2to3                    | 335 ms                                                 | 248 ms: 1.35x faster                                   |
| fannkuch                | 488 ms                                                 | 362 ms: 1.35x faster                                   |
| async_tree_none         | 711 ms                                                 | 530 ms: 1.34x faster                                   |
| aiohttp                 | 1.34 ms                                                | 1.00 ms: 1.34x faster                                  |
| scimark_fft             | 421 ms                                                 | 316 ms: 1.33x faster                                   |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.32x faster                                  |
| async_tree_memoization  | 855 ms                                                 | 646 ms: 1.32x faster                                   |
| deepcopy                | 438 us                                                 | 331 us: 1.32x faster                                   |
| deepcopy_reduce         | 3.79 us                                                | 2.90 us: 1.31x faster                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.20 ms: 1.30x faster                                  |
| async_tree_cpu_io_mixed | 949 ms                                                 | 731 ms: 1.30x faster                                   |
| genshi_xml              | 63.7 ms                                                | 49.1 ms: 1.30x faster                                  |
| sqlglot_normalize       | 134 ms                                                 | 104 ms: 1.29x faster                                   |
| sqlglot_optimize        | 65.2 ms                                                | 51.4 ms: 1.27x faster                                  |
| coroutines              | 31.6 ms                                                | 25.0 ms: 1.27x faster                                  |
| nqueens                 | 100 ms                                                 | 79.2 ms: 1.26x faster                                  |
| dulwich_log             | 75.8 ms                                                | 61.1 ms: 1.24x faster                                  |
| xml_etree_generate      | 93.8 ms                                                | 76.6 ms: 1.22x faster                                  |
| json_loads              | 28.7 us                                                | 23.8 us: 1.21x faster                                  |
| unpack_sequence         | 59.4 ns                                                | 50.2 ns: 1.18x faster                                  |
| sympy_integrate         | 24.0 ms                                                | 20.4 ms: 1.18x faster                                  |
| pylint                  | 532 ms                                                 | 454 ms: 1.17x faster                                   |
| sympy_expand            | 534 ms                                                 | 456 ms: 1.17x faster                                   |
| pickle_list             | 4.72 us                                                | 4.06 us: 1.16x faster                                  |
| sympy_str               | 325 ms                                                 | 280 ms: 1.16x faster                                   |
| regex_v8                | 25.0 ms                                                | 22.1 ms: 1.13x faster                                  |
| json                    | 5.35 ms                                                | 4.72 ms: 1.13x faster                                  |
| sqlite_synth            | 2.92 us                                                | 2.60 us: 1.12x faster                                  |
| sympy_sum               | 183 ms                                                 | 164 ms: 1.12x faster                                   |
| xml_etree_parse         | 163 ms                                                 | 146 ms: 1.12x faster                                   |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                  |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.11x faster                                   |
| xml_etree_iterparse     | 111 ms                                                 | 101 ms: 1.10x faster                                   |
| unpickle                | 14.2 us                                                | 13.0 us: 1.09x faster                                  |
| telco                   | 6.73 ms                                                | 6.32 ms: 1.07x faster                                  |
| mdp                     | 2.74 sec                                               | 2.59 sec: 1.06x faster                                 |
| regex_dna               | 214 ms                                                 | 203 ms: 1.05x faster                                   |
| generators              | 76.4 ms                                                | 73.8 ms: 1.04x faster                                  |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| pickle                  | 10.2 us                                                | 10.3 us: 1.01x slower                                  |
| unpickle_list           | 4.92 us                                                | 5.02 us: 1.02x slower                                  |
| python_startup_no_site  | 5.78 ms                                                | 6.06 ms: 1.05x slower                                  |
| regex_effbot            | 3.19 ms                                                | 3.60 ms: 1.13x slower                                  |
| pickle_dict             | 27.6 us                                                | 31.9 us: 1.16x slower                                  |
| coverage                | 74.7 ms                                                | 98.9 ms: 1.32x slower                                  |
| Geometric mean          | (ref)                                                  | 1.31x faster                                           |
Ignored benchmarks (13) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: async_generators, asyncio_tcp, bench_mp_pool, bench_thread_pool, create_gc_cycles, dask, djangocms, docutils, flaskblogging, gc_traversal, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221009-3.12.0a1+-2d2e01a/bm-20221009-linux-x86_64-python-main-3.12.0a1+-2d2e01a.json: mypy
