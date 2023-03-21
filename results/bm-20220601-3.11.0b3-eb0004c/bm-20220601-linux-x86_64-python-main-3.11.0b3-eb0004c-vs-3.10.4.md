
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: eb0004c
- commit date: 2022-06-01
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220601-linux-x86_64-python-main-3.11.0b3-eb0004c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 335 ms                                                 | 256 ms: 1.31x faster                                  |
| chameleon      | 9.17 ms                                                | 6.67 ms: 1.37x faster                                 |
| html5lib       | 85.9 ms                                                | 62.6 ms: 1.37x faster                                 |
| tornado_http   | 128 ms                                                 | 93.8 ms: 1.37x faster                                 |
| Geometric mean | (ref)                                                  | 1.36x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220601-linux-x86_64-python-main-3.11.0b3-eb0004c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 144 ms                                                 | 90.6 ms: 1.59x faster                                 |
| float          | 109 ms                                                 | 72.9 ms: 1.50x faster                                 |
| pidigits       | 190 ms                                                 | 194 ms: 1.02x slower                                  |
| Geometric mean | (ref)                                                  | 1.33x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220601-linux-x86_64-python-main-3.11.0b3-eb0004c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 135 ms: 1.31x faster                                  |
| regex_v8       | 25.0 ms                                                | 21.2 ms: 1.18x faster                                 |
| regex_dna      | 214 ms                                                 | 192 ms: 1.12x faster                                  |
| regex_effbot   | 3.19 ms                                                | 2.92 ms: 1.10x faster                                 |
| Geometric mean | (ref)                                                  | 1.17x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220601-linux-x86_64-python-main-3.11.0b3-eb0004c |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 302 us: 1.50x faster                                  |
| xml_etree_process    | 74.5 ms                                                | 53.8 ms: 1.39x faster                                 |
| unpickle_pure_python | 302 us                                                 | 228 us: 1.32x faster                                  |
| xml_etree_generate   | 93.8 ms                                                | 76.3 ms: 1.23x faster                                 |
| json_loads           | 28.7 us                                                | 24.4 us: 1.18x faster                                 |
| pickle_list          | 4.72 us                                                | 4.33 us: 1.09x faster                                 |
| pickle_dict          | 27.6 us                                                | 25.6 us: 1.08x faster                                 |
| json_dumps           | 13.4 ms                                                | 12.5 ms: 1.08x faster                                 |
| unpickle             | 14.2 us                                                | 13.3 us: 1.06x faster                                 |
| pickle               | 10.2 us                                                | 9.55 us: 1.06x faster                                 |
| xml_etree_iterparse  | 111 ms                                                 | 105 ms: 1.06x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 156 ms: 1.05x faster                                  |
| unpickle_list        | 4.92 us                                                | 4.89 us: 1.01x faster                                 |
| Geometric mean       | (ref)                                                  | 1.15x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220601-linux-x86_64-python-main-3.11.0b3-eb0004c |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.33 ms: 1.69x faster                                 |
| python_startup_no_site | 5.78 ms                                                | 6.17 ms: 1.07x slower                                 |
| Geometric mean         | (ref)                                                  | 1.26x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220601-linux-x86_64-python-main-3.11.0b3-eb0004c |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.82 ms: 1.49x faster                                 |
| django_template | 46.3 ms                                                | 32.9 ms: 1.41x faster                                 |
| Geometric mean  | (ref)                                                  | 1.45x faster                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220601-linux-x86_64-python-main-3.11.0b3-eb0004c |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.62 ms: 2.01x faster                                 |
| logging_silent          | 176 ns                                                 | 101 ns: 1.74x faster                                  |
| scimark_sor             | 197 ms                                                 | 115 ms: 1.71x faster                                  |
| python_startup          | 14.1 ms                                                | 8.33 ms: 1.69x faster                                 |
| go                      | 226 ms                                                 | 137 ms: 1.65x faster                                  |
| scimark_monte_carlo     | 109 ms                                                 | 66.0 ms: 1.65x faster                                 |
| pyflate                 | 676 ms                                                 | 411 ms: 1.64x faster                                  |
| richards                | 75.2 ms                                                | 46.5 ms: 1.62x faster                                 |
| raytrace                | 467 ms                                                 | 292 ms: 1.60x faster                                  |
| crypto_pyaes            | 117 ms                                                 | 73.1 ms: 1.60x faster                                 |
| nbody                   | 144 ms                                                 | 90.6 ms: 1.59x faster                                 |
| chaos                   | 106 ms                                                 | 66.9 ms: 1.58x faster                                 |
| spectral_norm           | 150 ms                                                 | 97.6 ms: 1.53x faster                                 |
| scimark_lu              | 161 ms                                                 | 107 ms: 1.51x faster                                  |
| pickle_pure_python      | 452 us                                                 | 302 us: 1.50x faster                                  |
| float                   | 109 ms                                                 | 72.9 ms: 1.50x faster                                 |
| hexiom                  | 9.43 ms                                                | 6.32 ms: 1.49x faster                                 |
| mako                    | 14.7 ms                                                | 9.82 ms: 1.49x faster                                 |
| django_template         | 46.3 ms                                                | 32.9 ms: 1.41x faster                                 |
| pycparser               | 1.53 sec                                               | 1.10 sec: 1.39x faster                                |
| xml_etree_process       | 74.5 ms                                                | 53.8 ms: 1.39x faster                                 |
| logging_format          | 8.85 us                                                | 6.44 us: 1.37x faster                                 |
| chameleon               | 9.17 ms                                                | 6.67 ms: 1.37x faster                                 |
| html5lib                | 85.9 ms                                                | 62.6 ms: 1.37x faster                                 |
| unpack_sequence         | 59.4 ns                                                | 43.4 ns: 1.37x faster                                 |
| tornado_http            | 128 ms                                                 | 93.8 ms: 1.37x faster                                 |
| thrift                  | 1.03 ms                                                | 759 us: 1.36x faster                                  |
| logging_simple          | 8.10 us                                                | 5.95 us: 1.36x faster                                 |
| scimark_fft             | 421 ms                                                 | 317 ms: 1.33x faster                                  |
| unpickle_pure_python    | 302 us                                                 | 228 us: 1.32x faster                                  |
| regex_compile           | 177 ms                                                 | 135 ms: 1.31x faster                                  |
| 2to3                    | 335 ms                                                 | 256 ms: 1.31x faster                                  |
| fannkuch                | 488 ms                                                 | 372 ms: 1.31x faster                                  |
| nqueens                 | 100 ms                                                 | 80.7 ms: 1.24x faster                                 |
| xml_etree_generate      | 93.8 ms                                                | 76.3 ms: 1.23x faster                                 |
| dulwich_log             | 75.8 ms                                                | 63.1 ms: 1.20x faster                                 |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.54 ms: 1.20x faster                                 |
| regex_v8                | 25.0 ms                                                | 21.2 ms: 1.18x faster                                 |
| json_loads              | 28.7 us                                                | 24.4 us: 1.18x faster                                 |
| sqlite_synth            | 2.92 us                                                | 2.49 us: 1.17x faster                                 |
| sympy_integrate         | 24.0 ms                                                | 20.5 ms: 1.17x faster                                 |
| sympy_sum               | 183 ms                                                 | 159 ms: 1.15x faster                                  |
| sympy_str               | 325 ms                                                 | 284 ms: 1.14x faster                                  |
| sympy_expand            | 534 ms                                                 | 467 ms: 1.14x faster                                  |
| json                    | 5.35 ms                                                | 4.75 ms: 1.13x faster                                 |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                 |
| regex_dna               | 214 ms                                                 | 192 ms: 1.12x faster                                  |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.10x faster                                  |
| regex_effbot            | 3.19 ms                                                | 2.92 ms: 1.10x faster                                 |
| pickle_list             | 4.72 us                                                | 4.33 us: 1.09x faster                                 |
| pickle_dict             | 27.6 us                                                | 25.6 us: 1.08x faster                                 |
| json_dumps              | 13.4 ms                                                | 12.5 ms: 1.08x faster                                 |
| unpickle                | 14.2 us                                                | 13.3 us: 1.06x faster                                 |
| pickle                  | 10.2 us                                                | 9.55 us: 1.06x faster                                 |
| xml_etree_iterparse     | 111 ms                                                 | 105 ms: 1.06x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 156 ms: 1.05x faster                                  |
| telco                   | 6.73 ms                                                | 6.49 ms: 1.04x faster                                 |
| unpickle_list           | 4.92 us                                                | 4.89 us: 1.01x faster                                 |
| pidigits                | 190 ms                                                 | 194 ms: 1.02x slower                                  |
| python_startup_no_site  | 5.78 ms                                                | 6.17 ms: 1.07x slower                                 |
| Geometric mean          | (ref)                                                  | 1.30x faster                                          |
Ignored benchmarks (35) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
