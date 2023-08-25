
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 951303f
- commit date: 2023-01-07
- overall geometric mean: 1.24x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230107-darwin-arm64-python-main-3.12.0a3+-951303f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 182 ms: 1.11x faster                                   |
| chameleon      | 5.84 ms                                                | 4.48 ms: 1.30x faster                                  |
| docutils       | 1.78 sec                                               | 1.43 sec: 1.25x faster                                 |
| html5lib       | 44.1 ms                                                | 34.7 ms: 1.27x faster                                  |
| Geometric mean | (ref)                                                  | 1.23x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230107-darwin-arm64-python-main-3.12.0a3+-951303f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 63.8 ms: 1.47x faster                                  |
| float          | 72.3 ms                                                | 51.6 ms: 1.40x faster                                  |
| pidigits       | 282 ms                                                 | 277 ms: 1.02x faster                                   |
| Geometric mean | (ref)                                                  | 1.28x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230107-darwin-arm64-python-main-3.12.0a3+-951303f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 75.2 ms: 1.29x faster                                  |
| regex_v8       | 17.5 ms                                                | 16.1 ms: 1.09x faster                                  |
| regex_dna      | 160 ms                                                 | 149 ms: 1.07x faster                                   |
| regex_effbot   | 2.45 ms                                                | 2.61 ms: 1.07x slower                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230107-darwin-arm64-python-main-3.12.0a3+-951303f |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 192 us: 1.47x faster                                   |
| unpickle_pure_python | 203 us                                                 | 142 us: 1.43x faster                                   |
| json_dumps           | 8.38 ms                                                | 6.10 ms: 1.37x faster                                  |
| xml_etree_process    | 45.1 ms                                                | 34.7 ms: 1.30x faster                                  |
| xml_etree_parse      | 107 ms                                                 | 92.8 ms: 1.16x faster                                  |
| xml_etree_generate   | 54.3 ms                                                | 48.5 ms: 1.12x faster                                  |
| xml_etree_iterparse  | 72.6 ms                                                | 66.2 ms: 1.10x faster                                  |
| unpickle             | 9.77 us                                                | 9.05 us: 1.08x faster                                  |
| json_loads           | 16.9 us                                                | 16.3 us: 1.04x faster                                  |
| unpickle_list        | 2.66 us                                                | 2.63 us: 1.01x faster                                  |
| pickle_list          | 2.83 us                                                | 2.86 us: 1.01x slower                                  |
| pickle_dict          | 17.8 us                                                | 18.0 us: 1.01x slower                                  |
| pickle               | 7.36 us                                                | 7.52 us: 1.02x slower                                  |
| Geometric mean       | (ref)                                                  | 1.14x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230107-darwin-arm64-python-main-3.12.0a3+-951303f |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 9.28 ms: 1.36x faster                                  |
| python_startup_no_site | 9.73 ms                                                | 7.32 ms: 1.33x faster                                  |
| Geometric mean         | (ref)                                                  | 1.34x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230107-darwin-arm64-python-main-3.12.0a3+-951303f |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.10 ms: 1.48x faster                                  |
| genshi_xml      | 37.6 ms                                                | 28.2 ms: 1.33x faster                                  |
| genshi_text     | 18.4 ms                                                | 14.3 ms: 1.29x faster                                  |
| django_template | 27.3 ms                                                | 21.3 ms: 1.28x faster                                  |
| Geometric mean  | (ref)                                                  | 1.34x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230107-darwin-arm64-python-main-3.12.0a3+-951303f |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 5.15 ms                                                | 2.56 ms: 2.01x faster                                  |
| logging_silent          | 119 ns                                                 | 64.9 ns: 1.84x faster                                  |
| richards                | 51.4 ms                                                | 30.4 ms: 1.69x faster                                  |
| scimark_sor             | 127 ms                                                 | 82.4 ms: 1.54x faster                                  |
| go                      | 165 ms                                                 | 108 ms: 1.53x faster                                   |
| scimark_lu              | 110 ms                                                 | 71.9 ms: 1.53x faster                                  |
| async_tree_memoization  | 493 ms                                                 | 328 ms: 1.50x faster                                   |
| raytrace                | 328 ms                                                 | 221 ms: 1.48x faster                                   |
| mako                    | 10.5 ms                                                | 7.10 ms: 1.48x faster                                  |
| nbody                   | 94.1 ms                                                | 63.8 ms: 1.47x faster                                  |
| pickle_pure_python      | 284 us                                                 | 192 us: 1.47x faster                                   |
| crypto_pyaes            | 78.0 ms                                                | 53.7 ms: 1.45x faster                                  |
| unpickle_pure_python    | 203 us                                                 | 142 us: 1.43x faster                                   |
| scimark_monte_carlo     | 72.2 ms                                                | 51.0 ms: 1.42x faster                                  |
| pyflate                 | 453 ms                                                 | 322 ms: 1.41x faster                                   |
| float                   | 72.3 ms                                                | 51.6 ms: 1.40x faster                                  |
| async_tree_none         | 402 ms                                                 | 287 ms: 1.40x faster                                   |
| pathlib                 | 28.8 ms                                                | 20.8 ms: 1.39x faster                                  |
| async_tree_io           | 1.02 sec                                               | 736 ms: 1.39x faster                                   |
| json_dumps              | 8.38 ms                                                | 6.10 ms: 1.37x faster                                  |
| python_startup          | 12.6 ms                                                | 9.28 ms: 1.36x faster                                  |
| deepcopy_memo           | 34.5 us                                                | 25.6 us: 1.35x faster                                  |
| pprint_pformat          | 1.24 sec                                               | 925 ms: 1.34x faster                                   |
| pycparser               | 915 ms                                                 | 685 ms: 1.34x faster                                   |
| pprint_safe_repr        | 609 ms                                                 | 455 ms: 1.34x faster                                   |
| thrift                  | 586 us                                                 | 439 us: 1.34x faster                                   |
| genshi_xml              | 37.6 ms                                                | 28.2 ms: 1.33x faster                                  |
| python_startup_no_site  | 9.73 ms                                                | 7.32 ms: 1.33x faster                                  |
| chaos                   | 66.8 ms                                                | 50.3 ms: 1.33x faster                                  |
| spectral_norm           | 96.4 ms                                                | 72.8 ms: 1.32x faster                                  |
| hexiom                  | 6.32 ms                                                | 4.78 ms: 1.32x faster                                  |
| logging_simple          | 4.63 us                                                | 3.52 us: 1.32x faster                                  |
| logging_format          | 5.01 us                                                | 3.81 us: 1.31x faster                                  |
| chameleon               | 5.84 ms                                                | 4.48 ms: 1.30x faster                                  |
| xml_etree_process       | 45.1 ms                                                | 34.7 ms: 1.30x faster                                  |
| dulwich_log             | 37.1 ms                                                | 28.7 ms: 1.29x faster                                  |
| genshi_text             | 18.4 ms                                                | 14.3 ms: 1.29x faster                                  |
| regex_compile           | 96.6 ms                                                | 75.2 ms: 1.29x faster                                  |
| sqlglot_transpile       | 1.54 ms                                                | 1.20 ms: 1.28x faster                                  |
| sqlglot_parse           | 1.33 ms                                                | 1.04 ms: 1.28x faster                                  |
| django_template         | 27.3 ms                                                | 21.3 ms: 1.28x faster                                  |
| deepcopy                | 278 us                                                 | 219 us: 1.27x faster                                   |
| html5lib                | 44.1 ms                                                | 34.7 ms: 1.27x faster                                  |
| deepcopy_reduce         | 2.38 us                                                | 1.91 us: 1.25x faster                                  |
| docutils                | 1.78 sec                                               | 1.43 sec: 1.25x faster                                 |
| async_tree_cpu_io_mixed | 670 ms                                                 | 541 ms: 1.24x faster                                   |
| fannkuch                | 317 ms                                                 | 258 ms: 1.23x faster                                   |
| scimark_sparse_mat_mult | 3.47 ms                                                | 2.82 ms: 1.23x faster                                  |
| sqlglot_optimize        | 38.0 ms                                                | 31.0 ms: 1.23x faster                                  |
| bench_thread_pool       | 548 us                                                 | 450 us: 1.22x faster                                   |
| unpack_sequence         | 38.7 ns                                                | 32.5 ns: 1.19x faster                                  |
| scimark_fft             | 232 ms                                                 | 195 ms: 1.19x faster                                   |
| sympy_integrate         | 13.4 ms                                                | 11.4 ms: 1.17x faster                                  |
| async_generators        | 233 ms                                                 | 200 ms: 1.16x faster                                   |
| sqlglot_normalize       | 197 ms                                                 | 170 ms: 1.16x faster                                   |
| xml_etree_parse         | 107 ms                                                 | 92.8 ms: 1.16x faster                                  |
| sympy_expand            | 276 ms                                                 | 241 ms: 1.14x faster                                   |
| nqueens                 | 68.1 ms                                                | 60.2 ms: 1.13x faster                                  |
| xml_etree_generate      | 54.3 ms                                                | 48.5 ms: 1.12x faster                                  |
| sympy_str               | 169 ms                                                 | 151 ms: 1.12x faster                                   |
| 2to3                    | 202 ms                                                 | 182 ms: 1.11x faster                                   |
| sympy_sum               | 94.3 ms                                                | 85.9 ms: 1.10x faster                                  |
| xml_etree_iterparse     | 72.6 ms                                                | 66.2 ms: 1.10x faster                                  |
| regex_v8                | 17.5 ms                                                | 16.1 ms: 1.09x faster                                  |
| json                    | 3.10 ms                                                | 2.84 ms: 1.09x faster                                  |
| sqlite_synth            | 1.47 us                                                | 1.35 us: 1.09x faster                                  |
| mdp                     | 1.67 sec                                               | 1.53 sec: 1.09x faster                                 |
| unpickle                | 9.77 us                                                | 9.05 us: 1.08x faster                                  |
| coroutines              | 20.2 ms                                                | 18.8 ms: 1.08x faster                                  |
| regex_dna               | 160 ms                                                 | 149 ms: 1.07x faster                                   |
| telco                   | 3.68 ms                                                | 3.47 ms: 1.06x faster                                  |
| json_loads              | 16.9 us                                                | 16.3 us: 1.04x faster                                  |
| meteor_contest          | 78.6 ms                                                | 76.3 ms: 1.03x faster                                  |
| pidigits                | 282 ms                                                 | 277 ms: 1.02x faster                                   |
| unpickle_list           | 2.66 us                                                | 2.63 us: 1.01x faster                                  |
| pickle_list             | 2.83 us                                                | 2.86 us: 1.01x slower                                  |
| pickle_dict             | 17.8 us                                                | 18.0 us: 1.01x slower                                  |
| generators              | 32.9 ms                                                | 33.7 ms: 1.02x slower                                  |
| pickle                  | 7.36 us                                                | 7.52 us: 1.02x slower                                  |
| bench_mp_pool           | 41.0 ms                                                | 41.9 ms: 1.02x slower                                  |
| regex_effbot            | 2.45 ms                                                | 2.61 ms: 1.07x slower                                  |
| coverage                | 40.8 ms                                                | 57.3 ms: 1.40x slower                                  |
| Geometric mean          | (ref)                                                  | 1.24x faster                                           |
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230107-3.12.0a3+-951303f/bm-20230107-darwin-arm64-python-main-3.12.0a3+-951303f.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.18x
