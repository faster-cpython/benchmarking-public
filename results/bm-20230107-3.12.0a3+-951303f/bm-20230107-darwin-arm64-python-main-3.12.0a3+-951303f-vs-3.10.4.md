
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 951303f
- commit date: 2023-01-07
- overall geometric mean: 1.24x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230107-darwin-arm64-python-main-3.12.0a3+-951303f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 182 ms: 1.10x faster                                   |
| chameleon      | 5.79 ms                                                | 4.48 ms: 1.29x faster                                  |
| docutils       | 1.78 sec                                               | 1.43 sec: 1.24x faster                                 |
| html5lib       | 44.2 ms                                                | 34.7 ms: 1.27x faster                                  |
| Geometric mean | (ref)                                                  | 1.23x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230107-darwin-arm64-python-main-3.12.0a3+-951303f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 63.8 ms: 1.46x faster                                  |
| float          | 72.4 ms                                                | 51.6 ms: 1.40x faster                                  |
| pidigits       | 282 ms                                                 | 277 ms: 1.02x faster                                   |
| Geometric mean | (ref)                                                  | 1.28x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230107-darwin-arm64-python-main-3.12.0a3+-951303f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 75.2 ms: 1.28x faster                                  |
| regex_v8       | 17.6 ms                                                | 16.1 ms: 1.09x faster                                  |
| regex_dna      | 162 ms                                                 | 149 ms: 1.08x faster                                   |
| regex_effbot   | 2.46 ms                                                | 2.61 ms: 1.06x slower                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230107-darwin-arm64-python-main-3.12.0a3+-951303f |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 192 us: 1.47x faster                                   |
| unpickle_pure_python | 203 us                                                 | 142 us: 1.43x faster                                   |
| json_dumps           | 8.40 ms                                                | 6.10 ms: 1.38x faster                                  |
| xml_etree_process    | 44.8 ms                                                | 34.7 ms: 1.29x faster                                  |
| xml_etree_parse      | 106 ms                                                 | 92.8 ms: 1.15x faster                                  |
| xml_etree_generate   | 54.2 ms                                                | 48.5 ms: 1.12x faster                                  |
| unpickle             | 9.89 us                                                | 9.05 us: 1.09x faster                                  |
| xml_etree_iterparse  | 72.3 ms                                                | 66.2 ms: 1.09x faster                                  |
| json_loads           | 16.9 us                                                | 16.3 us: 1.04x faster                                  |
| unpickle_list        | 2.69 us                                                | 2.63 us: 1.02x faster                                  |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.00x slower                                  |
| pickle_list          | 2.80 us                                                | 2.86 us: 1.02x slower                                  |
| pickle               | 7.35 us                                                | 7.52 us: 1.02x slower                                  |
| Geometric mean       | (ref)                                                  | 1.14x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230107-darwin-arm64-python-main-3.12.0a3+-951303f |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 9.28 ms: 1.28x faster                                  |
| python_startup_no_site | 8.88 ms                                                | 7.32 ms: 1.21x faster                                  |
| Geometric mean         | (ref)                                                  | 1.25x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230107-darwin-arm64-python-main-3.12.0a3+-951303f |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.10 ms: 1.48x faster                                  |
| genshi_xml      | 37.2 ms                                                | 28.2 ms: 1.32x faster                                  |
| genshi_text     | 18.4 ms                                                | 14.3 ms: 1.29x faster                                  |
| django_template | 27.3 ms                                                | 21.3 ms: 1.28x faster                                  |
| Geometric mean  | (ref)                                                  | 1.34x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230107-darwin-arm64-python-main-3.12.0a3+-951303f |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.56 ms: 2.01x faster                                  |
| logging_silent          | 119 ns                                                 | 64.9 ns: 1.84x faster                                  |
| richards                | 51.4 ms                                                | 30.4 ms: 1.69x faster                                  |
| go                      | 165 ms                                                 | 108 ms: 1.54x faster                                   |
| scimark_sor             | 126 ms                                                 | 82.4 ms: 1.53x faster                                  |
| scimark_lu              | 109 ms                                                 | 71.9 ms: 1.52x faster                                  |
| async_tree_memoization  | 490 ms                                                 | 328 ms: 1.49x faster                                   |
| mako                    | 10.5 ms                                                | 7.10 ms: 1.48x faster                                  |
| raytrace                | 325 ms                                                 | 221 ms: 1.47x faster                                   |
| pickle_pure_python      | 283 us                                                 | 192 us: 1.47x faster                                   |
| nbody                   | 93.3 ms                                                | 63.8 ms: 1.46x faster                                  |
| crypto_pyaes            | 78.1 ms                                                | 53.7 ms: 1.45x faster                                  |
| unpickle_pure_python    | 203 us                                                 | 142 us: 1.43x faster                                   |
| scimark_monte_carlo     | 72.5 ms                                                | 51.0 ms: 1.42x faster                                  |
| pyflate                 | 453 ms                                                 | 322 ms: 1.41x faster                                   |
| float                   | 72.4 ms                                                | 51.6 ms: 1.40x faster                                  |
| async_tree_none         | 400 ms                                                 | 287 ms: 1.40x faster                                   |
| pathlib                 | 28.8 ms                                                | 20.8 ms: 1.39x faster                                  |
| async_tree_io           | 1.02 sec                                               | 736 ms: 1.38x faster                                   |
| json_dumps              | 8.40 ms                                                | 6.10 ms: 1.38x faster                                  |
| deepcopy_memo           | 34.4 us                                                | 25.6 us: 1.34x faster                                  |
| pycparser               | 916 ms                                                 | 685 ms: 1.34x faster                                   |
| pprint_pformat          | 1.23 sec                                               | 925 ms: 1.33x faster                                   |
| pprint_safe_repr        | 606 ms                                                 | 455 ms: 1.33x faster                                   |
| chaos                   | 66.7 ms                                                | 50.3 ms: 1.33x faster                                  |
| hexiom                  | 6.32 ms                                                | 4.78 ms: 1.32x faster                                  |
| thrift                  | 580 us                                                 | 439 us: 1.32x faster                                   |
| genshi_xml              | 37.2 ms                                                | 28.2 ms: 1.32x faster                                  |
| sqlglot_parse           | 1.37 ms                                                | 1.04 ms: 1.32x faster                                  |
| spectral_norm           | 95.8 ms                                                | 72.8 ms: 1.32x faster                                  |
| logging_simple          | 4.63 us                                                | 3.52 us: 1.32x faster                                  |
| sqlglot_transpile       | 1.57 ms                                                | 1.20 ms: 1.31x faster                                  |
| logging_format          | 4.97 us                                                | 3.81 us: 1.30x faster                                  |
| chameleon               | 5.79 ms                                                | 4.48 ms: 1.29x faster                                  |
| dulwich_log             | 37.1 ms                                                | 28.7 ms: 1.29x faster                                  |
| xml_etree_process       | 44.8 ms                                                | 34.7 ms: 1.29x faster                                  |
| genshi_text             | 18.4 ms                                                | 14.3 ms: 1.29x faster                                  |
| deepcopy                | 281 us                                                 | 219 us: 1.29x faster                                   |
| python_startup          | 11.9 ms                                                | 9.28 ms: 1.28x faster                                  |
| regex_compile           | 96.4 ms                                                | 75.2 ms: 1.28x faster                                  |
| django_template         | 27.3 ms                                                | 21.3 ms: 1.28x faster                                  |
| html5lib                | 44.2 ms                                                | 34.7 ms: 1.27x faster                                  |
| deepcopy_reduce         | 2.37 us                                                | 1.91 us: 1.25x faster                                  |
| docutils                | 1.78 sec                                               | 1.43 sec: 1.24x faster                                 |
| async_tree_cpu_io_mixed | 669 ms                                                 | 541 ms: 1.24x faster                                   |
| fannkuch                | 317 ms                                                 | 258 ms: 1.23x faster                                   |
| sqlglot_optimize        | 38.0 ms                                                | 31.0 ms: 1.23x faster                                  |
| scimark_sparse_mat_mult | 3.46 ms                                                | 2.82 ms: 1.23x faster                                  |
| python_startup_no_site  | 8.88 ms                                                | 7.32 ms: 1.21x faster                                  |
| bench_thread_pool       | 546 us                                                 | 450 us: 1.21x faster                                   |
| scimark_fft             | 230 ms                                                 | 195 ms: 1.18x faster                                   |
| async_generators        | 234 ms                                                 | 200 ms: 1.17x faster                                   |
| sympy_integrate         | 13.3 ms                                                | 11.4 ms: 1.17x faster                                  |
| sqlglot_normalize       | 196 ms                                                 | 170 ms: 1.15x faster                                   |
| unpack_sequence         | 37.4 ns                                                | 32.5 ns: 1.15x faster                                  |
| xml_etree_parse         | 106 ms                                                 | 92.8 ms: 1.15x faster                                  |
| sympy_expand            | 275 ms                                                 | 241 ms: 1.14x faster                                   |
| nqueens                 | 68.2 ms                                                | 60.2 ms: 1.13x faster                                  |
| xml_etree_generate      | 54.2 ms                                                | 48.5 ms: 1.12x faster                                  |
| sympy_str               | 169 ms                                                 | 151 ms: 1.12x faster                                   |
| 2to3                    | 201 ms                                                 | 182 ms: 1.10x faster                                   |
| regex_v8                | 17.6 ms                                                | 16.1 ms: 1.09x faster                                  |
| unpickle                | 9.89 us                                                | 9.05 us: 1.09x faster                                  |
| sqlite_synth            | 1.47 us                                                | 1.35 us: 1.09x faster                                  |
| xml_etree_iterparse     | 72.3 ms                                                | 66.2 ms: 1.09x faster                                  |
| sympy_sum               | 93.6 ms                                                | 85.9 ms: 1.09x faster                                  |
| json                    | 3.08 ms                                                | 2.84 ms: 1.09x faster                                  |
| mdp                     | 1.66 sec                                               | 1.53 sec: 1.08x faster                                 |
| regex_dna               | 162 ms                                                 | 149 ms: 1.08x faster                                   |
| coroutines              | 20.2 ms                                                | 18.8 ms: 1.08x faster                                  |
| telco                   | 3.63 ms                                                | 3.47 ms: 1.05x faster                                  |
| json_loads              | 16.9 us                                                | 16.3 us: 1.04x faster                                  |
| meteor_contest          | 78.1 ms                                                | 76.3 ms: 1.02x faster                                  |
| unpickle_list           | 2.69 us                                                | 2.63 us: 1.02x faster                                  |
| pidigits                | 282 ms                                                 | 277 ms: 1.02x faster                                   |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.00x slower                                  |
| pickle_list             | 2.80 us                                                | 2.86 us: 1.02x slower                                  |
| pickle                  | 7.35 us                                                | 7.52 us: 1.02x slower                                  |
| generators              | 32.7 ms                                                | 33.7 ms: 1.03x slower                                  |
| bench_mp_pool           | 39.7 ms                                                | 41.9 ms: 1.06x slower                                  |
| regex_effbot            | 2.46 ms                                                | 2.61 ms: 1.06x slower                                  |
| coverage                | 42.0 ms                                                | 57.3 ms: 1.36x slower                                  |
| Geometric mean          | (ref)                                                  | 1.24x faster                                           |
Ignored benchmarks (13) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230107-3.12.0a3+-951303f/bm-20230107-darwin-arm64-python-main-3.12.0a3+-951303f.json: mypy
